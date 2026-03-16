# Mapping d'instruments modernes vers OPL3/GM compatibles
INSTRUMENT_MAP = {
    0: 0,   # Acoustic Grand Piano
    1: 0,   # Bright Piano → Grand Piano
    24: 24, # Nylon Guitar
    25: 24, # Steel Guitar → Nylon Guitar
    40: 40, # Violin
    41: 40, # Viola → Violin
    56: 56, # Trumpet
    57: 56, # Trombone → Trumpet
}

MAX_CHANNELS = 16

def map_instrument(program: int) -> int:
    """Retourne le programme compatible OPL3"""
    return INSTRUMENT_MAP.get(program, 0)

def channel_allowed(channel: int) -> bool:
    """Vérifie si le canal est utilisable sur OPL3"""
    return channel < MAX_CHANNELS