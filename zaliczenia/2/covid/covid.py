class NegativeHospitalBedsError(Exception):
    def __init__(self, beds: int) -> None:
        super().__init__("Number of hospital beds cannot be negative")
        self.__beds = beds


class Hospital():
    def __init__(self, city: str, covid: int, covid_icu: int, non_covid: int, non_covid_icu: int) -> None:
        self.__city = city
        if covid < 0:
            raise NegativeHospitalBedsError(covid)
        else:
            self.__covid = covid
        if covid_icu < 0:
            raise NegativeHospitalBedsError(covid_icu)
        else:
            self.__covid_icu = covid_icu
        if non_covid < 0:
            raise NegativeHospitalBedsError(non_covid)
        else:
            self.__non_covid = non_covid
        if non_covid_icu < 0:
            raise NegativeHospitalBedsError(non_covid_icu)
        else:
            self.__non_covid_icu = non_covid_icu

    @property
    def city(self) -> str:
        return self.__city

    @property
    def covid(self) -> int:
        return self.__covid

    @property
    def covid_icu(self) -> int:
        return self.__covid_icu

    @property
    def non_covid(self) -> int:
        return self.__non_covid

    @property
    def non_covid_icu(self) -> int:
        return self.__non_covid_icu

    def set_covid(self, new_covid: int) -> None:
        if new_covid < 0:
            raise NegativeHospitalBedsError(new_covid)
        else:
            self.__covid = new_covid

    def set_covid_icu(self, new_covid_icu: int) -> None:
        if new_covid_icu < 0:
            raise NegativeHospitalBedsError(new_covid_icu)
        else:
            self.__covid_icu = new_covid_icu

    def set_non_covid(self, new_non_covid: int) -> None:
        if new_non_covid < 0:
            raise NegativeHospitalBedsError(new_non_covid)
        else:
            self.__non_covid = new_non_covid

    def set_non_covid_icu(self, new_non_covid_icu: int) -> None:
        if new_non_covid_icu < 0:
            raise NegativeHospitalBedsError(new_non_covid_icu)
        else:
            self.__non_covid_icu = new_non_covid_icu

    def has_unoccupied_covid(self) -> bool:
        return self.__covid > 0

    def has_unoccupied_covid_icu(self) -> bool:
        return self.__covid_icu > 0

    def has_unoccupied_non_covid(self) -> bool:
        return self.__non_covid > 0

    def has_unoccupied_non_covid_icu(self) -> bool:
        return self.__non_covid_icu > 0

    def assign_covid(self) -> None:
        self.set_covid(self.__covid-1)

    def assign_covid_icu(self) -> None:
        self.set_covid(self.__covid - 1)
        self.set_covid_icu(self.__covid_icu - 1)

    def assign_non_covid(self) -> None:
        self.set_non_covid(self.__non_covid - 1)

    def assign_non_covid_icu(self) -> None:
        self.set_non_covid_icu(self.__non_covid_icu - 1)

    def __str__(self) -> str:
        covid_str = f"{self.__covid} covid beds"
        covid_icu_str = f"{self.__covid_icu} icu covid beds"
        non_covid_str = f"{self.non_covid} non-covid beds"
        non_covid_icu_str = f"{self.non_covid_icu} icu non-covid beds"
        return f"Hospital in {self.__city} has {covid_str}{covid_icu_str}{non_covid_str}{non_covid_icu_str}"


class Patient():
    def __init__(self, city: str, has_covid: bool, needs_icu: bool) -> None:
        self.__city = city
        self.__has_covid = has_covid
        self.__needs_icu = needs_icu

    @property
    def city(self) -> str:
        return self.__city

    @property
    def has_covid(self) -> bool:
        return self.__has_covid

    @property
    def needs_icu(self) -> bool:
        return self.__needs_icu

    def set_covid(self, has_covid: bool) -> None:
        self.__has_covid = has_covid

    def set_needs_icu(self, needs_icu: bool) -> None:
        self.__needs_icu = needs_icu


CITIES = {
    "Warsaw": {
        "hospital": Hospital("Warsaw", 1800, 400, 2200, 200),
        "other_cities": {"Siedlce": 93, "Radom": 103}
    },
    "Siedlce": {
        "hospital": Hospital("Siedlce", 335, 110, 455, 40),
        "other_cities": {"Warsaw": 93, "Radom": 182}
    },
    "Radom": {
        "hospital": Hospital("Radom", 300, 90, 200, 25),
        "other_cities": {"Warsaw": 103, "Siedlce": 182}
    }
}


def choose_hospital_covid_icu(closest_hospital, second_closest_hospital, third_closest_hospital):
    if closest_hospital.has_unoccupied_covid_icu():
        return closest_hospital
    else:
        if second_closest_hospital.has_unoccupied_covid_icu():
            return second_closest_hospital
        else:
            return third_closest_hospital


def choose_hospital_covid(closest_hospital, second_closest_hospital, third_closest_hospital):
    if closest_hospital.has_unoccupied_covid():
        return closest_hospital
    else:
        if second_closest_hospital.has_unoccupied_covid():
            return second_closest_hospital
        else:
            return third_closest_hospital


def choose_hospital_non_covid_icu(closest_hospital, second_closest_hospital, third_closest_hospital):
    if closest_hospital.has_unoccupied_non_covid_icu():
        return closest_hospital
    else:
        if second_closest_hospital.has_unoccupied_non_covid_icu():
            return second_closest_hospital
        else:
            return third_closest_hospital


def choose_hospital_non_covid(closest_hospital, second_closest_hospital, third_closest_hospital):
    if closest_hospital.has_unoccupied_non_covid():
        return closest_hospital
    else:
        if second_closest_hospital.has_unoccupied_non_covid():
            return second_closest_hospital
        else:
            return third_closest_hospital


def choose_hospital(patient: Patient):
    closest_hospital = CITIES[patient.city]["hospital"]
    needs_icu = patient.needs_icu
    has_covid = patient.has_covid
    other_cities_names = list(CITIES[patient.city]["other_cities"].keys())
    second_closest_city = other_cities_names[0]
    second_closest_hospital = CITIES[second_closest_city]["hospital"]
    third_closest_city = other_cities_names[1]
    third_closest_hospital = CITIES[third_closest_city]["hospital"]

    match (has_covid, needs_icu):
        case (True, True):
            chosen_hospital = choose_hospital_covid_icu(
                closest_hospital, second_closest_hospital,
                third_closest_hospital)
            chosen_hospital.assign_covid_icu()
        case(True, False):
            chosen_hospital = choose_hospital_covid(
                closest_hospital, second_closest_hospital,
                third_closest_hospital)
            chosen_hospital.assign_covid()
        case(False, True):
            chosen_hospital = choose_hospital_non_covid_icu(
                closest_hospital, second_closest_hospital,
                third_closest_hospital)
            chosen_hospital.assign_non_covid_icu()
        case(False, False):
            chosen_hospital = choose_hospital_non_covid(
                closest_hospital, second_closest_hospital,
                third_closest_hospital)
            chosen_hospital.assign_non_covid()

    return chosen_hospital


def main():
    # patient = Patient("Warsaw", True, True)
    # chosen_hospital = choose_hospital(patient)
    # print(chosen_hospital.city)



if __name__ == "__main__":
    main()
