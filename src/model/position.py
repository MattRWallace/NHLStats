from enum import Enum

"""
Enumeration to map positions to numerical values. Numerical values match those
used by the NHL API and should only be changed if the API changes.
"""
class Position(Enum):
    C = 1       # Center
    L = 2       # Left wing
    R = 3       # Right wing
    D = 4       # Defenseman
    G = 5       # Goalie