from main import calculate_distance
from Planet import Planet
import pytest


def test_calculate_distance_null():
    assert calculate_distance(Planet(0, 0, 0), Planet(0, 0, 0)) == 0


def test_calculate_distance_standard():
    assert calculate_distance(Planet(4, 0, 0), Planet(0, 0, 3)) == 5


def test_calculate_distance_invalid():
    with pytest.raises(ValueError):
        calculate_distance(Planet("a", 1, 1), Planet("b", 0, 0))
