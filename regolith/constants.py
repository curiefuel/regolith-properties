'''
Physical constants and reference values for regolith modeling.

All values from peer-reviewed literature with full citations.
'''

# Lunar regolith properties
# Source: Heiken, Vaniman & French (1991). Lunar Sourcebook.
LUNAR_PROPERTIES = {
    'thermal_conductivity_w_mk': {
        'mean': 0.0015,
        'std': 0.0005,
        'min': 0.0008,
        'max': 0.0025,
        'depth_dependence': 'increases with depth due to compaction',
        'source': 'Cremers & Hsia (1974), Lunar Sourcebook Ch.9',
    },
    'bulk_density_kg_m3': {
        'surface_mean': 1500,
        'surface_std': 150,
        'deep_mean': 1800,
        'deep_std': 100,
        'source': 'Mitchell et al. (1974), Lunar Sourcebook Ch.9',
    },
    'specific_heat_j_kg_k': {
        'mean': 840,
        'std': 40,
        'temp_dependence': True,
        'source': 'Hemingway et al. (1973)',
    },
    'thermal_diffusivity_m2_s': {
        'mean': 1.1e-6,
        'std': 2e-7,
        'source': 'Cremers (1975)',
    },
    'porosity': {
        'surface_mean': 0.45,
        'surface_std': 0.05,
        'deep_mean': 0.35,
        'deep_std': 0.03,
        'source': 'Carrier et al. (1991)',
    },
    'cohesion_pa': {
        'mean': 1000,
        'std': 500,
        'min': 100,
        'max': 3000,
        'source': 'Mitchell et al. (1974)',
    },
    'friction_angle_deg': {
        'mean': 42,
        'std': 5,
        'source': 'Mitchell et al. (1974)',
    },
    'bearing_capacity_kpa': {
        'mean': 150,
        'std': 50,
        'source': 'Heiken et al. (1991)',
    },
}

# Mars regolith properties
# Source: Golombek et al. (2018), InSight mission data
MARS_PROPERTIES = {
    'thermal_conductivity_w_mk': {
        'mean': 0.04,
        'std': 0.015,
        'min': 0.02,
        'max': 0.12,
        'depth_dependence': 'strongly increases below duricrust',
        'source': 'Golombek et al. (2018), Grott et al. (2021)',
    },
    'bulk_density_kg_m3': {
        'surface_mean': 1200,
        'surface_std': 200,
        'deep_mean': 1600,
        'deep_std': 150,
        'source': 'Herkenhoff et al. (2004)',
    },
    'specific_heat_j_kg_k': {
        'mean': 630,
        'std': 50,
        'source': 'Presley & Christensen (1997)',
    },
    'thermal_diffusivity_m2_s': {
        'mean': 5.3e-7,
        'std': 1e-7,
        'source': 'Mellon et al. (2000)',
    },
    'porosity': {
        'surface_mean': 0.50,
        'surface_std': 0.08,
        'deep_mean': 0.40,
        'deep_std': 0.05,
        'source': 'Clifford & Parker (2001)',
    },
    'cohesion_pa': {
        'mean': 500,
        'std': 300,
        'source': 'Moore et al. (1987)',
    },
    'friction_angle_deg': {
        'mean': 38,
        'std': 6,
        'source': 'Golombek et al. (2008)',
    },
    'bearing_capacity_kpa': {
        'mean': 100,
        'std': 40,
        'source': 'Golombek et al. (2018)',
    },
    'dust_particle_size_um': {
        'mean': 3.0,
        'std': 1.5,
        'source': 'Tomasko et al. (1999)',
    },
    'dust_deposition_rate_um_per_year': {
        'mean': 10,
        'std': 5,
        'source': 'Landis & Jenkins (2000)',
    },
}

# Apollo sample locations
APOLLO_SITES = {
    'Apollo_11': {'lat': 0.67, 'lon': 23.47, 'mare': True},
    'Apollo_12': {'lat': -3.01, 'lon': -23.42, 'mare': True},
    'Apollo_14': {'lat': -3.64, 'lon': -17.47, 'mare': False},
    'Apollo_15': {'lat': 26.13, 'lon': 3.63, 'mare': False},
    'Apollo_16': {'lat': -8.97, 'lon': 15.50, 'mare': False},
    'Apollo_17': {'lat': 20.19, 'lon': 30.77, 'mare': True},
}

# Mars landing sites
MARS_SITES = {
    'InSight': {'lat': 4.5, 'lon': 135.6, 'region': 'Elysium Planitia'},
    'Perseverance': {'lat': 18.4, 'lon': 77.7, 'region': 'Jezero Crater'},
    'Curiosity': {'lat': -4.6, 'lon': 137.4, 'region': 'Gale Crater'},
    'Opportunity': {'lat': -1.9, 'lon': 354.5, 'region': 'Meridiani Planum'},
}
