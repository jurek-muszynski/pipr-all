from polynomial import Polynomial
import pytest


def test_create_polynomial_standard():
    pol = Polynomial([(0, 4), (1, -2)])
    assert pol.coefficients == {0: 4, 1: -2}


def test_create_polynomial_zero():
    with pytest.raises(ValueError):
        Polynomial([(0, 4), (1, 0)])


def test_create_polynomial_indistinct():
    with pytest.raises(ValueError):
        Polynomial([(0, 4), (1, 1), (1, 3)])


def test_create_polynomial_negative_coefficient():
    with pytest.raises(ValueError):
        Polynomial([(0, 4), (-1, 0)])


def test_polynomial_get_coefficient_standard():
    pol = Polynomial([(0, 4), (1, -2)])
    assert pol.coefficient(0) == 4
    assert pol.coefficient(1) == -2


def test_polynomial_get_coefficient_invalid():
    pol = Polynomial([(0, 4), (1, -2)])
    with pytest.raises(KeyError):
        pol.coefficient(13)


def test_polynomial_get_degree_standard():
    pol_1 = Polynomial([(0, 4), (5, -2)])
    pol_2 = Polynomial([(0, 1)])
    assert pol_1.degree() == 5
    assert pol_2.degree() == 0


def test_polynomial_get_value():
    pol_1 = Polynomial([(0, 4)])
    pol_2 = Polynomial([(2, 1), (1, -4), (0, 4)])
    assert pol_1.value(1) == 4
    assert pol_1.value(0.5555) == 4
    assert pol_2.value(2) == 0
    assert pol_2.value(1) == 1


def test_polynomial_add_standard():
    pol_1 = Polynomial([(0, 4), (1, 3), (2, 1)])
    pol_2 = Polynomial([(0, 1), (1, 1), (2, 1)])
    pol_result = pol_1 + pol_2
    assert pol_result.coefficients == {0: 5, 1: 4, 2: 2}


def test_polynomial_add_different_coefficients():
    pol_1 = Polynomial([(0, 4), (1, 3), (2, 1)])
    pol_2 = Polynomial([(3, 1), (4, 1), (5, 1)])
    pol_result = pol_1 + pol_2
    assert pol_result.coefficients == {0: 4, 1: 3, 2: 1, 3: 1, 4: 1, 5: 1}


def test_polynomial_add_eliminating_coefficients():
    pol_1 = Polynomial([(0, -5), (2, 3), (3, 3), (7, 2)])
    pol_2 = Polynomial([(5, 3), (3, -3)])
    pol_result = pol_1 + pol_2
    assert pol_result.coefficients == {0: -5, 2: 3, 5: 3, 7: 2}


def test_polynomial_add_eliminating_coefficients_zero():
    pol_1 = Polynomial([(0, 4), (1, 3), (2, 1)])
    pol_2 = Polynomial([(0, -4), (1, -3), (2, -1)])
    pol_result = pol_1 + pol_2
    assert pol_result.coefficients == {0: 0}


def test_polynomial_subtract_standard():
    pol_1 = Polynomial([(0, 4), (1, 3), (2, 2)])
    pol_2 = Polynomial([(0, 3), (1, 2), (2, 1)])
    pol_result = pol_1 - pol_2
    assert pol_result.coefficients == {0: 1, 1: 1, 2: 1}


def test_polynomial_subtract_different_coefficients():
    pol_1 = Polynomial([(0, 4), (1, 3), (2, 2)])
    pol_2 = Polynomial([(3, 3), (4, 4), (5, 5)])
    pol_result = pol_1 - pol_2
    assert pol_result.coefficients == {0: 4, 1: 3, 2: 2, 3: -3, 4: -4, 5: -5}


def test_polynomial_str_std():
    pol_1 = Polynomial([(0, 4), (1, 3), (2, 2)])
    assert str(pol_1) == "2x^2+3x+4"


def test_polynomial_str_negative_coefficients():
    pol_1 = Polynomial([(0, -4), (1, -3), (2, -2)])
    assert str(pol_1) == "-2x^2-3x-4"


def test_polynomial_str_mixed_coefficients():
    pol_1 = Polynomial([(0, -4), (1, 3), (2, 2), (3, -3)])
    assert str(pol_1) == "-3x^3+2x^2+3x-4"


def test_polynomial_str_single_coefficient():
    pol_1 = Polynomial([(0, 1)])
    assert str(pol_1) == "1"
    pol_2 = Polynomial([(4, 2)])
    assert str(pol_2) == "2x^4"
    pol_3 = Polynomial([(2, -2)])
    assert str(pol_3) == "-2x^2"


def test_polynomial_str_zero():
    pol_1 = Polynomial([(0, 0)])
    assert str(pol_1) == "0"
