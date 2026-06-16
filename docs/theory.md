# Regolith Properties: Theoretical Background

## Lunar Regolith Formation

Lunar regolith is the product of billions of years of micrometeorite bombardment, solar wind sputtering, and thermal cycling in vacuum. Unlike terrestrial soils formed by chemical weathering, lunar regolith is a mechanical fragmentation product with no water content and minimal chemical alteration. This formation mechanism produces several key characteristics:

**Depth-dependent compaction**: The regolith density increases with depth due to overburden pressure and impact-induced compaction. Surface regolith (~0-10cm) has bulk densities around 1500 kg/m³, while material below 1-2 meters approaches 1800 kg/m³. This compaction profile is critical for FSP reactor burial calculations, as bearing capacity scales directly with density.

**Grain size distribution**: Lunar regolith exhibits a fractal grain size distribution from sub-micron dust to centimeter-scale rock fragments, with the modal size around 60-80 microns. This size distribution maximizes surface area per unit volume, which in vacuum creates an extremely effective thermal insulator at the surface.

**Porosity variation**: Surface porosity ranges from 40-50%, decreasing to 30-35% at depth. This porosity dominates the thermal conductivity behavior, as radiation across vacuum-filled pores is the rate-limiting heat transfer mechanism.

## Apollo Sample Measurement Methodology

Apollo missions 11, 12, 14, 15, 16, and 17 returned 382 kg of regolith samples measured under controlled laboratory conditions. Thermal property measurements employed three primary techniques:

**Steady-state thermal conductivity**: Samples were placed between heated and cooled plates in vacuum chambers at 10⁻⁶ torr. Temperature gradients were measured with thermocouples after reaching steady state. This technique revealed the strong density dependence of conductivity, with values ranging from 0.0008 W/m/K for loose surface fines to 0.0025 W/m/K for compacted deep samples.

**Differential scanning calorimetry (DSC)**: Specific heat was measured from 90K to 400K, revealing the strong temperature dependence captured in the Hemingway et al. (1973) polynomial. The positive temperature coefficient arises from increased lattice vibration modes in silicate minerals as temperature rises.

**Mechanical testing**: Bearing capacity and shear strength were measured using miniature penetrometers and direct shear boxes on both returned samples and in-situ during Apollo surface operations. The Mohr-Coulomb failure criterion with cohesion ~1 kPa and friction angle ~42° accurately describes the mechanical behavior.

## Uncertainty Sources

Several factors contribute to property uncertainty:

1. **Sample disturbance**: Core tube sampling disturbed the in-situ density structure, particularly for deep samples
2. **Compositional variation**: Mare basalts vs highland anorthosites exhibit 10-20% property variation
3. **Measurement precision**: Thermal conductivity measurements at 10⁻⁶ torr have ±15-25% uncertainty due to residual gas conduction
4. **Depth extrapolation**: Properties below the ~3m maximum core depth are extrapolated from compaction models

These uncertainties are quantified in the `RegolithUncertaintyAnalysis` class using Monte Carlo sampling.

## Thermal Conductivity Physics in Vacuum

Lunar regolith thermal conductivity is uniquely dominated by solid-phase conduction through the network of grain contacts and radiative transfer across vacuum-filled pores. In vacuum (pressure < 10⁻⁶ torr), gas-phase conduction is negligible, leaving:

**k_total = k_solid + k_radiative**

where:
- k_solid ≈ φ² × k_grain × (contact area fraction)
- k_radiative ≈ 4σT³ × pore size × emissivity

The solid-phase term scales with the square of density (φ²) because both the number of contacts and the contact area increase with compaction. This quadratic dependence explains why surface regolith (low density) has thermal conductivity ~3× lower than deep compacted regolith.

The radiative term becomes significant above ~300K, where T³ scaling causes k to increase with temperature. This radiative contribution is why the effective conductivity is temperature-dependent in thermal models.

## Mars vs Lunar Thermal Conductivity

Martian regolith exhibits thermal conductivity 5-50× higher than lunar regolith despite similar bulk density and grain size. This dramatic difference arises from the thin CO₂ atmosphere (600 Pa vs <10⁻¹² Pa lunar):

**Gas-phase conduction**: At 600 Pa CO₂, gas conduction contributes ~0.02 W/m/K even in highly porous regolith. This adds directly to the solid-phase and radiative terms, dominating the total conductivity for typical Martian conditions.

**Duricrust cementation**: Many Martian sites exhibit a near-surface duricrust layer (0-5cm depth) where salts and ice have cemented grains together. This cementation increases grain contact area, raising the solid-phase conductivity by 2-3×. The duricrust layer is critical for lander stability but complicates burial operations.

**InSight HP³ measurements**: The InSight Heat Flow and Physical Properties Probe (HP³) measured in-situ thermal conductivity by monitoring temperature decay after pulse heating. Values of 0.04-0.06 W/m/K were measured in the upper ~35cm, consistent with models of loose basaltic sand with gas-phase conduction.

## Bearing Capacity for Reactor Burial

FSP reactor burial requires excavating regolith and placing the reactor pressure vessel below the surface for radiation shielding and thermal coupling. The bearing capacity must support the reactor mass without excessive settlement.

**Mohr-Coulomb failure criterion**: Regolith shear strength follows τ = c + σ tan(φ), where:
- τ = shear stress at failure
- c = cohesion (lunar ~1 kPa, Mars ~0.5 kPa)
- σ = normal stress
- φ = friction angle (lunar ~42°, Mars ~38°)

**Bearing capacity calculation**: For a shallow foundation, Terzaghi's bearing capacity equation gives:

q_ult = c N_c + γ D N_q + 0.5 γ B N_γ

where:
- N_c, N_q, N_γ = bearing capacity factors (functions of φ)
- γ = regolith unit weight
- D = burial depth
- B = foundation width

For FSP reactors (mass ~2000 kg, footprint ~2 m²), a safety factor of 3 requires burial depths of 0.4-0.8m on the Moon and 0.6-1.0m on Mars.

## Why Regolith Uncertainty Matters for FSP Design

FSP reactor thermal design couples strongly to regolith properties:

**Heat rejection interface**: The reactor pressure vessel rejects ~20-40 kW of waste heat through the regolith to a surface radiator or heat pipe network. The temperature drop across the regolith layer scales inversely with thermal conductivity: ΔT = Q/(k×A). Lunar thermal conductivity uncertainty of ±25% translates directly to ±25% uncertainty in interface temperature, affecting reactor operating efficiency.

**Burial depth optimization**: Deeper burial provides better radiation shielding but requires excavating denser regolith and increases thermal resistance. The optimal depth balances these factors, but uncertainty in bearing capacity and thermal conductivity can shift the optimum by ±20-30cm. This uncertainty must be captured in site selection analysis.

**Long-term stability**: Regolith properties evolve over mission lifetime due to thermal cycling, radiation damage, and (on Mars) dust deposition. A 10-year Mars surface mission accumulates ~100 microns of dust on radiators, degrading emissivity by 8-15%. Uncertainty in deposition rates affects radiator sizing and mission lifetime predictions.

## References

- Heiken, G.H., Vaniman, D.T., French, B.M. (1991). *Lunar Sourcebook: A User's Guide to the Moon*. Cambridge University Press. [Chapters 7, 9]

- Carrier, W.D., Olhoeft, G.R., Mendell, W. (1991). Physical properties of the lunar surface. *Lunar Sourcebook*, 475-594.

- Cremers, C.J. (1975). Thermophysical properties of Apollo 14 fines. *Journal of Heat Transfer*, 97(4), 610-612.

- Hemingway, B.S., Robie, R.A., Wilson, W.H. (1973). Specific heats of lunar soils, basalt, and breccias from the Apollo 14, 15, and 16 landing sites. *Proc. Lunar Sci. Conf. 4th*, 2481-2487.

- Mitchell, J.K., Houston, W.N., Scott, R.F., et al. (1974). Mechanical properties of lunar soil: Density, porosity, cohesion, and angle of internal friction. *Proc. Lunar Sci. Conf. 3rd*, 3235-3253.

- Golombek, M., et al. (2018). Geology and physical properties investigations by the InSight lander. *Space Science Reviews*, 214(5), 84.

- Grott, M., et al. (2021). Thermal conductivity of the Martian soil at the InSight landing site from HP³ active heating experiments. *52nd Lunar and Planetary Science Conference*, Abstract #1837.

- Presley, M.A., Christensen, P.R. (1997). Thermal conductivity measurements of particulate materials: 2. Results. *Journal of Geophysical Research: Planets*, 102(E3), 6551-6566.

- Terzaghi, K. (1943). *Theoretical Soil Mechanics*. Wiley. [Classic reference for bearing capacity theory]
