import zadanie1
import pytest


def test_sum_of_subsequence_typical():
    assert zadanie1.sum_of_subsequence([0, 0, 0, 1, 1, 1], 3) == [1, 1, 1]


def test_sum_of_subsequence_invalid_length():
    with pytest.raises(ValueError):
        zadanie1.sum_of_subsequence([1], 2)


def test_sum_of_subsequence_invalid_list():
    with pytest.raises(TypeError):
        zadanie1.sum_of_subsequence(["123"], "1")
