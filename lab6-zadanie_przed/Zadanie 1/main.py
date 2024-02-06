from Planet import Planet
import math


def calculate_distance(planet1: Planet, planet2: Planet) -> float:
    """
    calculates distance between two planets with 3-dimensional
    (x,y,z) coordinates
    """
    return math.sqrt((planet2.get_X() - planet1.get_X())**2 +
                     (planet2.get_Y() - planet1.get_Y())**2 +
                     (planet2.get_Z() - planet1.get_Z())**2)
