'''
Lunar South Pole Regolith Analysis
Artemis landing site characterization for FSP deployment.
'''

from regolith import LunarRegolith
import numpy as np

print('=== LUNAR SOUTH POLE REGOLITH ANALYSIS ===')

reg = LunarRegolith(depth_m=0.0, latitude_deg=-89.5)

print('\nSURFACE PROPERTIES')
for k, v in reg.summary().items():
    print(f'  {k}: {v}')

print('\nOPTIMAL BURIAL DEPTH FOR 2000kg REACTOR')
depth = reg.optimal_burial_depth_m(reactor_mass_kg=2000, footprint_m2=2.0)
print(f'  Minimum burial depth: {depth:.2f} m')

print('\nTEMPERATURE PROFILE (south pole, 24hr cycle)')
print(f'{"Hour":>6} {"Surface Temp (K)":>18}')
for hour in range(0, 25, 4):
    T = reg.surface_temperature_k(time_of_day_hours=hour)
    print(f'{hour:>6} {T:>18.1f}')

print('\nSPECIFIC HEAT VS TEMPERATURE')
print(f'{"Temp (K)":>10} {"cp (J/kg/K)":>12}')
for T in [100, 150, 200, 250, 300, 350, 400]:
    cp = reg.specific_heat_j_kg_k(temp_k=T)
    print(f'{T:>10} {cp:>12.1f}')
