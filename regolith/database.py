'''
Unified regolith property database interface.

Single entry point for accessing lunar and Mars regolith
properties with consistent API across both bodies.
'''

from .lunar import LunarRegolith
from .mars import MarsRegolith
from .uncertainty import RegolithUncertaintyAnalysis


def get_properties(body: str, depth_m: float = 0.0, **kwargs):
    '''
    Get regolith properties for a given body and depth.

    Args:
        body: 'lunar' or 'mars'
        depth_m: depth below surface in meters
        **kwargs: passed to LunarRegolith or MarsRegolith

    Returns:
        LunarRegolith or MarsRegolith instance
    '''
    if body == 'lunar':
        return LunarRegolith(depth_m=depth_m, **kwargs)
    elif body == 'mars':
        return MarsRegolith(depth_m=depth_m, **kwargs)
    raise ValueError(f'Unknown body: {body}. Use lunar or mars.')


def fsp_site_assessment(body: str,
                         depth_m: float = 0.5,
                         reactor_mass_kg: float = 2000) -> dict:
    '''
    Complete site assessment for FSP deployment.
    Returns all properties relevant to reactor siting.
    '''
    reg = get_properties(body, depth_m)
    ua = RegolithUncertaintyAnalysis(body=body, depth_m=depth_m)

    return {
        'body': body,
        'depth_m': depth_m,
        'properties': reg.summary(),
        'uncertainty': {
            'thermal_conductivity': ua.thermal_conductivity_distribution(),
            'bearing_capacity': ua.bearing_capacity_distribution(),
        },
        'burial_risk': ua.reactor_burial_risk(depth_m, reactor_mass_kg),
        'recommendation': (
            'SUITABLE' if ua.reactor_burial_risk(depth_m, reactor_mass_kg) < 0.05
            else 'FURTHER ANALYSIS REQUIRED'
        ),
    }
