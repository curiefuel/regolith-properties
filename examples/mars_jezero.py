'''
Mars Jezero Crater Regolith Analysis
Perseverance landing site characterization for FSP deployment.
'''

from regolith import MarsRegolith
import numpy as np

print('=== MARS JEZERO CRATER REGOLITH ANALYSIS ===')

reg = MarsRegolith(depth_m=0.0, region='jezero_crater', has_duricrust=True)

print('\nSURFACE PROPERTIES (with duricrust)')
for k, v in reg.summary().items():
    print(f'  {k}: {v}')

print('\nDUST DEPOSITION IMPACT ON RADIATORS')
years = [0, 1, 5, 10, 20]
print(f'{"Year":>6} {"Dust (mm)":>12} {"Efficiency Loss (%)":>22}')
for year in years:
    dust_mm = reg.dust_accumulation_mm_per_year() * year
    loss_pct = reg.radiator_efficiency_loss_per_year() * year * 100
    print(f'{year:>6} {dust_mm:>12.3f} {loss_pct:>22.2f}')

print('\nTHERMAL CONDUCTIVITY DEPTH PROFILE')
print('(shows duricrust layer transition)')
print(f'{"Depth (cm)":>12} {"k (W/m/K)":>12} {"Layer":>15}')
for depth_cm in [0, 1, 2, 3, 4, 5, 6, 8, 10, 20, 50, 100]:
    depth_m = depth_cm / 100.0
    reg_depth = MarsRegolith(depth_m=depth_m, region='jezero_crater', has_duricrust=True)
    k = reg_depth.thermal_conductivity_w_mk()
    layer = 'duricrust' if depth_m < 0.05 else 'loose regolith'
    print(f'{depth_cm:>12} {k:>12.4f} {layer:>15}')

print('\nDIURNAL TEMPERATURE CYCLE')
print(f'{"Hour":>6} {"Northern Summer (K)":>22} {"Northern Winter (K)":>22}')
for hour in range(0, 25, 3):
    T_summer = reg.surface_temperature_k(time_of_day_hours=hour, season='northern_summer')
    T_winter = reg.surface_temperature_k(time_of_day_hours=hour, season='northern_winter')
    print(f'{hour:>6} {T_summer:>22.1f} {T_winter:>22.1f}')

print('\nBEARING CAPACITY VS DEPTH')
print(f'{"Depth (m)":>10} {"Capacity (kPa)":>16}')
for depth in np.arange(0, 2.1, 0.25):
    reg_depth = MarsRegolith(depth_m=depth, region='jezero_crater')
    capacity = reg_depth.bearing_capacity_kpa()
    print(f'{depth:>10.2f} {capacity:>16.1f}')

print('\nCOMPARISON: WITH vs WITHOUT DURICRUST')
print(f'{"Property":>30} {"With Duricrust":>18} {"Without Duricrust":>20}')
reg_with = MarsRegolith(depth_m=0.02, has_duricrust=True)
reg_without = MarsRegolith(depth_m=0.02, has_duricrust=False)
print(f'{"Thermal conductivity (W/m/K)":>30} {reg_with.thermal_conductivity_w_mk():>18.4f} {reg_without.thermal_conductivity_w_mk():>20.4f}')
print(f'{"Bearing capacity (kPa)":>30} {reg_with.bearing_capacity_kpa():>18.1f} {reg_without.bearing_capacity_kpa():>20.1f}')
