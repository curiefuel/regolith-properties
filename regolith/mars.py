'''
Martian regolith property models.

Based on InSight HP³ measurements, Curiosity REMS data,
and Perseverance surface characterization.

References:
- Grott et al. (2021). Lunar and Planetary Science Conference.
- Golombek et al. (2018). Space Science Reviews.
- Presley & Christensen (1997). JGR Planets.
'''

import numpy as np
from dataclasses import dataclass
from typing import Optional
from .constants import MARS_PROPERTIES


@dataclass
class MarsRegolith:
    '''
    Martian regolith property model.

    Key differences from lunar:
    - Higher thermal conductivity (thin CO2 atmosphere conducts)
    - Dust deposition degrades surface hardware
    - Duricrust layer affects mechanical properties
    - Diurnal temperature swings smaller but still significant
    '''

    depth_m: float = 0.0
    region: str = 'elysium_planitia'
    has_duricrust: bool = True
    duricrust_depth_m: float = 0.05

    def thermal_conductivity_w_mk(self) -> float:
        '''
        Depth and duricrust dependent thermal conductivity.

        Duricrust (0-5cm): ~0.08 W/m/K (cemented)
        Below duricrust:   ~0.04 W/m/K (loose)
        Deep (>1m):        ~0.10 W/m/K (compacted basalt)

        Source: Grott et al. (2021)
        '''
        if self.has_duricrust and self.depth_m < self.duricrust_depth_m:
            return 0.08
        k_surface = 0.04
        k_deep = 0.10
        z_scale = 0.8
        return k_surface + (k_deep - k_surface) * (1 - np.exp(-self.depth_m / z_scale))

    def specific_heat_j_kg_k(self, temp_k: float = 220.0) -> float:
        '''
        Temperature-dependent specific heat for basaltic regolith.
        Source: Presley & Christensen (1997)
        '''
        T = np.clip(temp_k, 150, 300)
        return 502 + 0.59 * T

    def bulk_density_kg_m3(self) -> float:
        rho_surface = 1200
        rho_deep = 1600
        z_scale = 0.5
        return rho_surface + (rho_deep - rho_surface) * (1 - np.exp(-self.depth_m / z_scale))

    def thermal_diffusivity_m2_s(self, temp_k: float = 220.0) -> float:
        k = self.thermal_conductivity_w_mk()
        cp = self.specific_heat_j_kg_k(temp_k)
        rho = self.bulk_density_kg_m3()
        return k / (rho * cp)

    def dust_accumulation_mm_per_year(self) -> float:
        '''
        Dust deposition rate from orbital observations.
        Source: Landis & Jenkins (2000)
        '''
        rates = {
            'elysium_planitia': 0.01,
            'jezero_crater': 0.008,
            'gale_crater': 0.012,
            'meridiani_planum': 0.009,
        }
        return rates.get(self.region, 0.01)

    def radiator_efficiency_loss_per_year(self) -> float:
        '''
        Fractional emissivity loss per year from dust.
        Critical parameter for FSP radiator lifetime planning.
        '''
        dust_mm = self.dust_accumulation_mm_per_year()
        return dust_mm * 0.008

    def bearing_capacity_kpa(self) -> float:
        base = 100.0
        if self.has_duricrust and self.depth_m < self.duricrust_depth_m:
            base = 300.0
        return base * (1 + self.depth_m * 2.0)

    def surface_temperature_k(self, time_of_day_hours: float = 12.0,
                               season: str = 'northern_summer') -> float:
        '''
        Diurnal surface temperature model.
        Source: REMS instrument, Curiosity rover
        '''
        T_means = {
            'northern_summer': 230,
            'northern_winter': 200,
        }
        T_mean = T_means.get(season, 220)
        T_amp = 50
        phase = 2 * np.pi * time_of_day_hours / 24.6  # Mars sol length
        return T_mean + T_amp * np.sin(phase - np.pi/2)

    def sample_thermal_conductivity(self, rng: np.random.Generator) -> float:
        nominal = self.thermal_conductivity_w_mk()
        return max(0.01, rng.normal(nominal, nominal * 0.20))

    def sample_bearing_capacity(self, rng: np.random.Generator) -> float:
        nominal = self.bearing_capacity_kpa()
        return max(20.0, rng.normal(nominal, nominal * 0.30))

    def summary(self) -> dict:
        return {
            'depth_m': self.depth_m,
            'region': self.region,
            'thermal_conductivity_w_mk': round(self.thermal_conductivity_w_mk(), 4),
            'specific_heat_j_kg_k': round(self.specific_heat_j_kg_k(), 1),
            'bulk_density_kg_m3': round(self.bulk_density_kg_m3(), 1),
            'thermal_diffusivity_m2_s': f'{self.thermal_diffusivity_m2_s():.2e}',
            'bearing_capacity_kpa': round(self.bearing_capacity_kpa(), 1),
            'dust_accumulation_mm_yr': self.dust_accumulation_mm_per_year(),
            'radiator_efficiency_loss_pct_yr': round(
                self.radiator_efficiency_loss_per_year() * 100, 3),
        }
