from Zadanie2 import distance, distance_one_dimension
import pytest


def test_distance_the_same():
    assert distance(10, (2, 3), (2, 3)) == 0


def test_distance_NE_NE_1():
    assert distance(10, (2, 3), (5, 1)) == 5


def test_distance_NE_NE_2():
    assert distance(20, (7, 3), (4, 5)) == 5


def test_distance_NW_NW_1():
    assert distance(15, (-5, 4), (-2, 5)) == 4


def test_distance_NW_NW_2():
    assert distance(10, (-5, 4), (-2, 5)) == 4


def test_distance_SE_SE_1():
    assert distance(12, (-3, 4), (-5, 1)) == 5


def test_distance_SE_SE_2():
    assert distance(12, (-4, 1), (-3, 3)) == 3


def test_distance_SW_SW_1():
    assert distance(14, (-8, -4), (-2, -6)) == 8


def test_distance_SW_SW_2():
    assert distance(14, (-2, -6), (-5, -2)) == 7


def test_distance_NE_SE():
    assert distance(10, (2, 4), (5, -2)) == 9


def test_distance_NE_SE_around():
    assert distance(10, (2, 6), (5, -8)) == 10


def test_distance_NW_SW():
    assert distance(14, (-2, 6), (-5, 2)) == 7


def test_distance_NW_SW_around():
    assert distance(14, (-2, 8), (-5, -9)) == 15


def test_distance_NW_NE():
    assert distance(14, (-2, 6), (5, 2)) == 11


def test_distance_NW_NE_around():
    assert distance(14, (-2, 6), (13, 2)) == 18


def test_distance_SW_SE():
    assert distance(14, (-2, -6), (5, -2)) == 11


def test_distance_SW_SE_around():
    assert distance(14, (-13, -6), (5, -2)) == 15


def test_distance_one_dimension_the_same():
    assert distance_one_dimension(10, 0, 0) == 0


def test_distance_one_dimension_typical():
    assert distance_one_dimension(10, 0, 5) == 5


def test_distance_one_dimension_negative():
    assert distance_one_dimension(10, -5, -1) == 4


def test_distance_one_dimension_positive():
    assert distance_one_dimension(10, 5, 1) == 4


def test_distance_one_dimension_around():
    assert distance_one_dimension(10, -10, 10) == 1


def test_distance_one_dimension_string():
    with pytest.raises(TypeError):
        distance_one_dimension(10, "1", 2)


def test_distance_one_dimension_null_size():
    with pytest.raises(IndexError):
        distance_one_dimension(0, 1, 0)


def test_distance_one_dimension_out_of_range():
    with pytest.raises(IndexError):
        distance_one_dimension(10, 11, 0)
    with pytest.raises(IndexError):
        distance_one_dimension(10, -11, 0)
