from offices import Office, RENT
import pytest


def test_create_office_standard():
    office = Office("Warszawa", 700, 10, 1)
    assert office.city == "Warszawa"
    assert office.area == 700
    assert office.rooms == 10
    assert office.branch == 1


def test_create_office_invalid():
    with pytest.raises(ValueError):
        Office("Warszawa", -700, 10, 1)
    with pytest.raises(ValueError):
        Office("", 700, 10, 1)
    with pytest.raises(ValueError):
        Office("Warszawa", 700, -10, 1)


def test_max_people_per_office():
    office = Office("Warszawa", 700, 10, 1)
    assert office.max_people() == 20


def test_monthly_office_costs():
    office = Office("Warszawa", 700, 10, 1)
    assert office.monthly_costs() == 70000
