RENT = {
    # price in zl for a square meter in particular citiess
    "Warszawa": 100,
    "Kraków": 70,
    "Poznań": 45,
    "Białystok": 30
}

MAX_PEOPLE_PER_ROOM = 2
MIN_METERS_PER_PERSON = 15


class Office():
    """
    Office class. Contains attributes:

    :param city: city, where the office is located
    :type city: str

    :param area: office's area in sq metres
    :type area: float

    :param rooms: number of room's in an office
    :type rooms: int

    :param branch: branch number
    :type branch: int

    """

    def __init__(self, city: str, area: float, rooms: int, branch: int) -> None:
        """
        Creates an office object.
        Raises ValueError if area or rooms are negative
        """
        if not city:
            raise ValueError("City's name cannot be empty")
        else:
            self.__city = city
        if area < 0:
            raise ValueError("Area cannot be negative")
        else:
            self.__area = float(area)
        if rooms < 0:
            raise ValueError("Number of rooms cannot be negative")
        else:
            self.__rooms = int(rooms)
        self.__branch = branch

    @property
    def city(self) -> str:
        return self.__city

    @property
    def area(self) -> float:
        return self.__area

    @property
    def rooms(self) -> int:
        return self.__rooms

    @property
    def branch(self) -> int:
        return self.__branch

    def max_people(self) -> int:
        """
        Returns the amount of people in an office so that
        self distancing is properly maintained
        """
        requirement_rooms = self.__rooms * MAX_PEOPLE_PER_ROOM
        requirement_area = self.__area // MIN_METERS_PER_PERSON
        return min(requirement_rooms, requirement_area)

    def monthly_costs(self) -> float:
        """
        Returns monthly costs for an office,
        based on a global dictionary with rent prices
        """
        price_per_meter = RENT.get(self.__city)
        return price_per_meter * self.__area
