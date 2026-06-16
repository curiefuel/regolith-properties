'''
Uncertainty quantification for regolith property sampling.

Provides Monte Carlo sampling across regolith property uncertainty
for FSP site selection and system design analysis.
'''

import numpy as np
from dataclasses import dataclass
from typing import Union
from .lunar import LunarRegolith
from .mars import MarsRegolith


class RegolithUncertaintyAnalysis:
    '''
    Monte Carlo analysis of regolith property uncertainty
    and its impact on FSP system performance.
    '''

    def __init__(self, body: str = 'lunar',
                 depth_m: float = 0.5,
                 n_samples: int = 10000,
                 seed: int = 42):
        self.body = body
        self.depth_m = depth_m
        self.n_samples = n_samples
        self.rng = np.random.default_rng(seed)

    def _get_regolith(self):
        if self.body == 'lunar':
            return LunarRegolith(depth_m=self.depth_m)
        return MarsRegolith(depth_m=self.depth_m)

    def thermal_conductivity_distribution(self) -> dict:
        reg = self._get_regolith()
        samples = np.array([
            reg.sample_thermal_conductivity(self.rng)
            for _ in range(self.n_samples)
        ])
        return {
            'mean': float(np.mean(samples)),
            'std': float(np.std(samples)),
            'p5': float(np.percentile(samples, 5)),
            'p95': float(np.percentile(samples, 95)),
            'unit': 'W/m/K',
        }

    def bearing_capacity_distribution(self) -> dict:
        reg = self._get_regolith()
        samples = np.array([
            reg.sample_bearing_capacity(self.rng)
            for _ in range(self.n_samples)
        ])
        return {
            'mean': float(np.mean(samples)),
            'std': float(np.std(samples)),
            'p5': float(np.percentile(samples, 5)),
            'p95': float(np.percentile(samples, 95)),
            'unit': 'kPa',
        }

    def reactor_burial_risk(self, target_depth_m: float = 0.5,
                             reactor_mass_kg: float = 2000) -> float:
        '''
        Probability that bearing capacity is insufficient
        for reactor burial at target depth.
        '''
        reg = self._get_regolith()
        footprint_m2 = 2.0
        pressure_kpa = (reactor_mass_kg * 1.62) / (footprint_m2 * 1000)
        required_kpa = pressure_kpa * 3.0

        failures = sum(
            1 for _ in range(self.n_samples)
            if reg.sample_bearing_capacity(self.rng) < required_kpa
        )
        return failures / self.n_samples

    def summary(self) -> None:
        print(f'\n=== REGOLITH UNCERTAINTY ANALYSIS ===')
        print(f'Body: {self.body} | Depth: {self.depth_m}m | Samples: {self.n_samples:,}')

        k = self.thermal_conductivity_distribution()
        print(f'\nTHERMAL CONDUCTIVITY')
        print(f'  Mean:  {k["mean"]:.5f} W/m/K')
        print(f'  Std:   {k["std"]:.5f} W/m/K')
        print(f'  P5-P95: {k["p5"]:.5f} – {k["p95"]:.5f} W/m/K')

        b = self.bearing_capacity_distribution()
        print(f'\nBEARING CAPACITY')
        print(f'  Mean:  {b["mean"]:.1f} kPa')
        print(f'  Std:   {b["std"]:.1f} kPa')
        print(f'  P5-P95: {b["p5"]:.1f} – {b["p95"]:.1f} kPa')

        risk = self.reactor_burial_risk()
        print(f'\nREACTOR BURIAL RISK')
        print(f'  Probability of insufficient bearing: {risk:.1%}')
