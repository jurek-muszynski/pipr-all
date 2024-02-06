class Planet:

    """
    Planet class. Contains attributes:

    :param name: planet's name
    :type name: str

    :param moons: number of planet's moons
    :type moons: int

    :param X: planet's x coordinate
    :type X: float

    :param Y: planet's y coordinate
    :type Y: float

    :param Z: planet's z coordinate
    :type Z: float
    """

    def __init__(self, x: float, y: float, z: float, name: str = "") -> None:
        self._X = float(x)
        self._Y = float(y)
        self._Z = float(z)
        self._moons = 0
        self._name = name.title()

    def get_name(self) -> str:
        return self._name

    def get_X(self) -> float:
        return self._X

    def get_Y(self) -> float:
        return self._Y

    def get_Z(self) -> float:
        return self._Z

    def get_moons(self) -> int:
        return self._moons

    def set_name(self, name: str) -> None:
        if not name:
            raise ValueError("Planet's name cannot be empty")
        else:
            self._name = name.title()

    def set_X(self, x: float) -> None:
        self._X = float(x)

    def set_Y(self, y: float) -> None:
        self._Y = float(y)

    def set_Z(self, z: float) -> None:
        self._Z = float(z)

    def set_moons(self, moons: int) -> None:
        moons = int(moons)
        if (moons < 0):
            raise ValueError("Number of moons cannot be negative")
        else:
            self._moons = moons

    def info(self) -> str:
        """
        returns some basic info about
        a planet (name, location, num of moons)

        """
        coordinates = f"it's located at ({self._X},{self._Y},{self._Z})"
        moon = "moon" if self._moons == 1 else "moons"
        moons = f"and has {self._moons} {moon}"
        return f"The planet's name is {self._name}, {coordinates} {moons}"

    def __str__(self) -> str:
        return self.info()
