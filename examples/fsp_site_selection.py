'''
FSP Site Selection Analysis
Curiefuel regolith-properties example

Compares lunar south pole vs Mars Jezero Crater
for FSP reactor deployment suitability.
'''

from regolith import fsp_site_assessment, LunarRegolith, MarsRegolith
from regolith.uncertainty import RegolithUncertaintyAnalysis
import numpy as np

print('=== CURIEFUEL FSP SITE SELECTION ANALYSIS ===')

# Lunar south pole assessment
print('\n--- LUNAR SOUTH POLE ---')
lunar = fsp_site_assessment('lunar', depth_m=0.5, reactor_mass_kg=2000)
print(f'Recommendation: {lunar["recommendation"]}')
print(f'Burial risk: {lunar["burial_risk"]:.1%}')
for k, v in lunar['properties'].items():
    print(f'  {k}: {v}')

# Mars Jezero assessment
print('\n--- MARS JEZERO CRATER ---')
mars = fsp_site_assessment('mars', depth_m=0.5, reactor_mass_kg=2000)
print(f'Recommendation: {mars["recommendation"]}')
print(f'Burial risk: {mars["burial_risk"]:.1%}')
for k, v in mars['properties'].items():
    print(f'  {k}: {v}')

# Depth profile comparison
print('\n--- THERMAL CONDUCTIVITY VS DEPTH ---')
print(f'{"Depth (m)":>10} {"Lunar (W/m/K)":>15} {"Mars (W/m/K)":>14}')
print('-' * 42)
for depth in np.arange(0, 2.1, 0.25):
    l = LunarRegolith(depth_m=depth).thermal_conductivity_w_mk()
    m = MarsRegolith(depth_m=depth).thermal_conductivity_w_mk()
    print(f'{depth:>10.2f} {l:>15.5f} {m:>14.4f}')

# Uncertainty analysis
print('\n--- UNCERTAINTY ANALYSIS: LUNAR SOUTH POLE ---')
ua = RegolithUncertaintyAnalysis(body='lunar', depth_m=0.5, n_samples=10000)
ua.summary()

print('\n--- UNCERTAINTY ANALYSIS: MARS JEZERO ---')
ua_mars = RegolithUncertaintyAnalysis(body='mars', depth_m=0.5, n_samples=10000)
ua_mars.summary()
