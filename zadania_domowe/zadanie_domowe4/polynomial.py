class Polynomial():
    """
    Polynomial class. Contains attributes:

    :param coefficients: polynomial's coefficients
    :type coefficients: dict[int]
    """

    def __init__(self, coefficients: list = []) -> None:
        coeffs = []
        for coeff, value in coefficients:
            if value == 0 and coeff != 0:
                raise ValueError("Value cannot be null")
            if coeff < 0:
                raise ValueError("Coefficient cannot be negative")
            if coeff in coeffs:
                raise ValueError("Coefficients cannot be repeated")
            coeffs.append(coeff)
        self.__coefficients = {coeff: value for coeff, value in coefficients}

    @property
    def coefficients(self) -> dict[int]:
        return self.__coefficients

    def degree(self) -> int:
        """
        Returns the degree of the polynomial
        """
        return max(self.__coefficients.keys())

    def coefficient(self, power: int) -> int | float:
        """
        Returns the value of the coefficient next to a specified power
        """
        return self.__coefficients[power]

    def value(self, x_value: int | float) -> int | float:
        """
        Returns the value of the polynomial for a given argument
        """
        result = 0
        for coeff in self.__coefficients:
            val = self.__coefficients[coeff]
            if coeff == 0:
                result += val
            else:
                result += (x_value ** coeff * val)
        return result

    def __add__(self, polynomial):
        """
        Addition of polynomials
        """
        coefficients_result = []
        coefficients_keys = set(
            polynomial.coefficients.keys() | self.__coefficients.keys())
        for coeff in coefficients_keys:
            value = self.__coefficients.get(
                coeff, 0) + polynomial.coefficients.get(coeff, 0)
            if value != 0 or coeff == 0:
                coefficients_result.append((coeff, value))
        return Polynomial(coefficients_result)

    def __sub__(self, polynomial):
        """
        Subtraction of polynomials
        """
        coefficients_result = []
        coefficients_keys = set(
            polynomial.coefficients.keys() | self.__coefficients.keys())
        for coeff in coefficients_keys:
            value = self.__coefficients.get(
                coeff, 0) - polynomial.coefficients.get(coeff, 0)
            if value != 0 or coeff == 0:
                coefficients_result.append((coeff, value))
        return Polynomial(coefficients_result)

    def __str__(self) -> str:
        polynomial_str = ""
        coefficient_keys = list(self.__coefficients.keys())[::-1]
        for coeff in coefficient_keys:
            value = self.__coefficients[coeff]
            sign = "+" if value > 0 else ""
            if coefficient_keys.index(coeff) != 0:
                polynomial_str += sign
            if coeff == 0:
                polynomial_str += f"{value}"
            elif coeff == 1:
                polynomial_str += f"{value}x"
            else:
                polynomial_str += f"{value}x^{coeff}"
        return polynomial_str
