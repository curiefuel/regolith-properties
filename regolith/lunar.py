'''
Lunar regolith property models.

Provides temperature-dependent and depth-dependent thermal and
mechanical properties for lunar regolith, with uncertainty bounds
derived from Apollo sample measurements.

References:
- Heiken, Vaniman & French (1991). Lunar Sourcebook. Cambridge.
- Cremers & Hsia (1974). Thermal conductivity of Apollo 15 fines.
- Mitchell et al. (1974). Mechanical properties of lunar soil.
- Carrier, Olhoeft & Mendell (1991). Physical properties of lunar surface.
'''

import numpy as np
from dataclasses import dataclass
from typing import Optional
from .constants import LUNAR_PROPERTIES, APOLLO_SITES


@dataclass
class LunarRegolith:
    '''
    Lunar regolith property model for a specific site and depth.

    Used for:
    - FSP reactor thermal interface modeling
    - Reactor burial depth optimization
    - Landing pad bearing capacity assessment
    - Heat pipe ground anchor design
    '''

    depth_m: float = 0.0
    latitude_deg: float = -89.5   # default: lunar south pole
    longitude_deg: float = 0.0
    apollo_site: Optional[str] = None

    def thermal_conductivity_w_mk(self) -> float:
        '''
        Depth-dependent thermal conductivity.

        Near surface: ~0.0008 W/m/K (highly porous, vacuum)
        Deep (>2m):   ~0.0025 W/m/K (compacted)

        k(z) = k_surface + (k_deep - k_surface) * (1 - exp(-z/z_scale))
        '''
        k_surface = 0.0008
        k_deep = 0.0025
        z_scale = 0.5
        return k_surface + (k_deep - k_surface) * (1 - np.exp(-self.depth_m / z_scale))

    def specific_heat_j_kg_k(self, temp_k: float = 250.0) -> float:
        '''
        Temperature-dependent specific heat.

        cp(T) = -23.173 + 2.127T + 1.5009e-2*T² - 7.3699e-5*T³ + 9.6552e-8*T⁴
        Valid range: 90K - 400K

        Source: Hemingway et al. (1973)
        '''
        T = np.clip(temp_k, 90, 400)
        return (-23.173 + 2.127*T + 1.5009e-2*T**2
                - 7.3699e-5*T**3 + 9.6552e-8*T**4)

    def bulk_density_kg_m3(self) -> float:
        '''
        Depth-dependent bulk density.

        rho(z) = rho_surface + (rho_deep - rho_surface) * (1 - exp(-z/z_scale))

        Source: Mitchell et al. (1974)
        '''
        rho_surface = 1500
        rho_deep = 1800
        z_scale = 0.3
        return rho_surface + (rho_deep - rho_surface) * (1 - np.exp(-self.depth_m / z_scale))

    def thermal_diffusivity_m2_s(self, temp_k: float = 250.0) -> float:
        k = self.thermal_conductivity_w_mk()
        cp = self.specific_heat_j_kg_k(temp_k)
        rho = self.bulk_density_kg_m3()
        return k / (rho * cp)

    def bearing_capacity_kpa(self) -> float:
        '''
        Bearing capacity for surface hardware foundations.
        Increases with depth due to confining pressure.
        '''
        base = 150.0
        depth_factor = 1 + self.depth_m * 2.5
        return base * depth_factor

    def shear_strength_kpa(self, normal_stress_kpa: float = 10.0) -> float:
        '''
        Mohr-Coulomb shear strength.
        tau = c + sigma * tan(phi)
        '''
        c = 1.0   # cohesion kPa
        phi = np.radians(42)
        return c + normal_stress_kpa * np.tan(phi)

    def optimal_burial_depth_m(self, reactor_mass_kg: float = 2000,
                                footprint_m2: float = 2.0) -> float:
        '''
        Minimum depth at which bearing capacity supports reactor mass.
        Returns depth where bearing capacity = reactor pressure * safety factor.
        '''
        pressure_kpa = (reactor_mass_kg * 1.62) / (footprint_m2 * 1000)
        safety_factor = 3.0
        required_kpa = pressure_kpa * safety_factor

        for depth in np.arange(0, 3.0, 0.01):
            self.depth_m = depth
            if self.bearing_capacity_kpa() >= required_kpa:
                return depth
        return 3.0

    def surface_temperature_k(self, time_of_day_hours: float = 12.0) -> float:
        '''
        Surface temperature as function of local time.
        Simplified sinusoidal model for equatorial regions.
        Poles use constant cold temperature.
        '''
        if abs(self.latitude_deg) > 85:
            return 220.0
        T_mean = 250
        T_amp = 140
        phase = 2 * np.pi * time_of_day_hours / 24
        return T_mean + T_amp * np.sin(phase - np.pi/2)

    def sample_thermal_conductivity(self, rng: np.random.Generator) -> float:
        nominal = self.thermal_conductivity_w_mk()
        return max(0.0005, rng.normal(nominal, nominal * 0.25))

    def sample_bearing_capacity(self, rng: np.random.Generator) -> float:
        nominal = self.bearing_capacity_kpa()
        return max(10.0, rng.normal(nominal, nominal * 0.25))

    def sample_bulk_density(self, rng: np.random.Generator) -> float:
        nominal = self.bulk_density_kg_m3()
        return max(1000, rng.normal(nominal, 100))

    def summary(self) -> dict:
        return {
            'depth_m': self.depth_m,
            'latitude_deg': self.latitude_deg,
            'thermal_conductivity_w_mk': round(self.thermal_conductivity_w_mk(), 5),
            'specific_heat_j_kg_k': round(self.specific_heat_j_kg_k(), 1),
            'bulk_density_kg_m3': round(self.bulk_density_kg_m3(), 1),
            'thermal_diffusivity_m2_s': f'{self.thermal_diffusivity_m2_s():.2e}',
            'bearing_capacity_kpa': round(self.bearing_capacity_kpa(), 1),
        }
