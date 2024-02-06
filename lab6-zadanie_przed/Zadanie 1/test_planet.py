from Planet import Planet
import pytest


def test_create_planet_standard():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.get_name() == "Jupiter"
    assert planet.get_X() == 0
    assert planet.get_Y() == 0
    assert planet.get_Z() == 0


def test_create_planet_no_name():
    planet = Planet(0, 0, 0)
    assert planet.get_name() == ""


def test_create_planet_no_coordinates():
    with pytest.raises(TypeError):
        Planet()


def test_planet_description():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.info() == "The planet's name is Jupiter, it's located at (0.0,0.0,0.0) and has 0 moons"


def test_planet_description_as_string():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.info() == str(planet)


def test_set_planets_name_standard():
    planet = Planet(0, 0, 0)
    assert planet.get_name() == ""
    planet.set_name("Jupiter")
    assert planet.get_name() == "Jupiter"
    planet.set_name("Earth")
    assert planet.get_name() == "Earth"


def test_set_planets_name_empty():
    planet = Planet(0, 0, 0)
    assert planet.get_name() == ""
    with pytest.raises(ValueError):
        planet.set_name("")


def test_set_planets_name_lowercase():
    planet = Planet(0, 0, 0)
    assert planet.get_name() == ""
    planet.set_name("jupiter")
    assert planet.get_name() == "Jupiter"


def test_set_planets_moons_standard():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.info() == "The planet's name is Jupiter, it's located at (0.0,0.0,0.0) and has 0 moons"
    planet.set_moons(2)
    assert planet.get_moons() == 2
    assert planet.info() == "The planet's name is Jupiter, it's located at (0.0,0.0,0.0) and has 2 moons"


def test_set_planets_moons_negative():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.get_moons() == 0
    with pytest.raises(ValueError):
        planet.set_moons(-1)


def test_set_planets_moons_float():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.get_moons() == 0
    planet.set_moons(2.234)
    assert planet.get_moons() == 2


def test_set_planets_moons_str():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.get_moons() == 0
    with pytest.raises(ValueError):
        planet.set_moons("2.32")


def test_set_planets_coordinates_standard():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.get_X() == 0
    assert planet.get_Y() == 0
    assert planet.get_Z() == 0
    planet.set_X(4.25)
    planet.set_Y(1.25)
    planet.set_Z(0.25)
    assert planet.get_X() == 4.25
    assert planet.get_Y() == 1.25
    assert planet.get_Z() == 0.25


def test_set_planets_coordinates_str():
    planet = Planet(0, 0, 0, "Jupiter")
    assert planet.get_X() == 0
    assert planet.get_Y() == 0
    assert planet.get_Z() == 0
    with pytest.raises(ValueError):
        planet.set_X("1.25.")
    planet.set_X("4.25")
    planet.set_Y("1.25")
    planet.set_Z("0.25")
    assert planet.get_X() == 4.25
    assert planet.get_Y() == 1.25
    assert planet.get_Z() == 0.25
