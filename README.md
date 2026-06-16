# regolith-properties

> Lunar and Martian regolith thermal and mechanical property database with uncertainty bounds. Compiled from Apollo samples, Chang'e data, and published literature. Built by Curiefuel for surface nuclear power system design.

## Overview

`regolith-properties` provides physics-based models of lunar and Martian regolith thermal and mechanical properties, derived from Apollo sample measurements, InSight HP³ data, and peer-reviewed literature. Designed for FSP (Fission Surface Power) reactor site selection, thermal interface design, and mission planning.

## Installation

```bash
pip install regolith-properties
```

Or install from source:

```bash
git clone https://github.com/curiefuel/regolith-properties.git
cd regolith-properties
pip install -e .
```

## Quick Start

```python
from regolith import fsp_site_assessment, LunarRegolith, MarsRegolith

# FSP site assessment for lunar south pole
lunar = fsp_site_assessment('lunar', depth_m=0.5, reactor_mass_kg=2000)
print(f"Recommendation: {lunar['recommendation']}")
print(f"Burial risk: {lunar['burial_risk']:.1%}")

# Get regolith properties at a specific depth
reg = LunarRegolith(depth_m=0.5, latitude_deg=-89.5)
print(f"Thermal conductivity: {reg.thermal_conductivity_w_mk():.5f} W/m/K")
print(f"Bearing capacity: {reg.bearing_capacity_kpa():.1f} kPa")

# Mars regolith with duricrust layer
mars = MarsRegolith(depth_m=0.5, region='jezero_crater')
print(f"Dust accumulation: {mars.dust_accumulation_mm_per_year():.3f} mm/yr")
```

## Features

- **Temperature-dependent thermal properties**: specific heat, thermal conductivity, thermal diffusivity
- **Depth-dependent mechanical properties**: bulk density, bearing capacity, shear strength
- **Uncertainty quantification**: Monte Carlo sampling across property uncertainty bounds
- **FSP-specific models**: reactor burial depth optimization, radiator dust degradation
- **Validated against Apollo samples**: all lunar properties traced to Apollo core samples and Lunar Sourcebook
- **Mars InSight HP³ data**: thermal conductivity from InSight mole penetration experiments

## Examples

See `examples/` directory:

- `fsp_site_selection.py` — compare lunar vs Mars sites for FSP deployment
- `lunar_south_pole.py` — detailed analysis of lunar south pole regolith
- `mars_jezero.py` — Mars Jezero Crater site characterization

## Documentation

- `docs/theory.md` — physics background and model derivations
- `docs/validation.md` — comparison with Apollo sample measurements
- `docs/sources.md` — complete bibliography and data sources

## References

- Heiken, Vaniman & French (1991). *Lunar Sourcebook*. Cambridge University Press.
- Cremers & Hsia (1974). Thermal conductivity of Apollo 15 fines. *Proc. Lunar Sci. Conf. 5th*.
- Golombek et al. (2018). Geology and physical properties investigations by the InSight lander. *Space Science Reviews*.
- Grott et al. (2021). Thermal conductivity of the Martian soil at the InSight landing site. *LPSC*.

## License

MIT

## Contact

Built by **Curiefuel** — nuclear energy for space exploration.

- Web: [curiefuel.com](https://curiefuel.com)
- GitHub: [@curiefuel](https://github.com/curiefuel)
- Email: hello@curiefuel.com
# regolith-properties
