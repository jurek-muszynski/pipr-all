from classes import Employee, Mandate_Contract_Employee, Full_Time_Employee, Software_Developer, Manager
from classes import NegativeSalaryError, NegativeWageError, NegativeHrsError
import pytest


def test_create_employee_standard():
    employee = Employee("Adam", "Smith", "example@you.com")
    assert employee.email == "example@you.com"
    assert employee.first_name == "Adam"
    assert employee.last_name == "Smith"


def test_employee_set_attributes_standard():
    employee = Employee("Adam", "Smith", "example@you.com")
    assert employee.email == "example@you.com"
    assert employee.first_name == "Adam"
    assert employee.last_name == "Smith"
    employee.set_email("example2@you.com")
    employee.set_first_name("Mark")
    employee.set_last_name("Jackson")
    assert employee.email == "example2@you.com"
    assert employee.first_name == "Mark"
    assert employee.last_name == "Jackson"


def test_create_full_time_employee_standard():
    employee = Full_Time_Employee(
        "Adam", "Smith", "example@you.com", 1000.50)
    assert employee.email == "example@you.com"
    assert employee.first_name == "Adam"
    assert employee.last_name == "Smith"
    assert employee.salary == 1000.50


def test_create_full_time_employee_negative_salary():
    with pytest.raises(NegativeSalaryError):
        Full_Time_Employee("Adam", "Smith", "example@you.com", -10)


def test_full_time_employee_set_salary_standard():
    employee = Full_Time_Employee(
        "Adam", "Smith", "example@you.com", 1000.50)
    assert employee.salary == 1000.50
    employee.set_salary(1100.50)
    assert employee.salary == 1100.50


def test_full_time_employee_set_negative_salary():
    employee = Full_Time_Employee(
        "Adam", "Smith", "example@you.com", 1000.50)
    assert employee.salary == 1000.50
    with pytest.raises(NegativeSalaryError):
        employee.set_salary(-1000)


def test_create_software_dev_standard():
    employee = Software_Developer(
        "Adam", "Smith", "example@you.com", 1000, "java")
    assert employee.language == "java"


def test_create_mandate_contract_employee_standard():
    employee = Mandate_Contract_Employee(
        "Adam", "Smith", "example@you.com", 26, 20)
    assert employee.wage == 26
    assert employee.hours == 20


def test_create_mandate_contract_employee_negative_values():
    with pytest.raises(NegativeWageError):
        Mandate_Contract_Employee("Adam", "Smith", "example@you.com", -10, 10)
    with pytest.raises(NegativeHrsError):
        Mandate_Contract_Employee("Adam", "Smith", "example@you.com", 10, -10)


def test_mandate_contract_employee_set_wage_standard():
    employee = Mandate_Contract_Employee(
        "Adam", "Smith", "example@you.com", 26, 20)
    assert employee.wage == 26
    employee.set_wage(26.50)
    assert employee.wage == 26.50


def test_mandate_contract_employee_set_negative_wage():
    employee = Mandate_Contract_Employee(
        "Adam", "Smith", "example@you.com", 26, 20)
    assert employee.wage == 26
    with pytest.raises(NegativeWageError):
        employee.set_wage(-26.50)


def test_mandate_contract_employee_set_hours_standard():
    employee = Mandate_Contract_Employee(
        "Adam", "Smith", "example@you.com", 26, 20)
    assert employee.hours == 20
    employee.set_hours(30)
    assert employee.hours == 30


def test_mandate_contract_employee_set_negative_hours():
    employee = Mandate_Contract_Employee(
        "Adam", "Smith", "example@you.com", 26, 20)
    assert employee.hours == 20
    with pytest.raises(NegativeHrsError):
        employee.set_hours(-30)


def test_mandate_contract_employee_calculate_salary_standard():
    employee = Mandate_Contract_Employee(
        "Adam", "Smith", "example@you.com", 26, 20)
    assert employee.calculate_salary() == 520


def test_create_software_developer_standard():
    employee = Software_Developer(
        "Adam", "Smith", "example@you.com", 1000.50, "java")
    assert employee.language == "java"


def test_software_developer_set_language_standard():
    employee = Software_Developer(
        "Adam", "Smith", "example@you.com", 1000.50, "java")
    assert employee.language == "java"
    employee.set_language("c++")
    assert employee.language == "c++"


def test_create_manager_standard():
    employees_list = [
        Employee("John", "Wayne", "john@wayne.com"),
        Software_Developer("Steve", "Norman",
                           "setve@norman.com", 1000.50, "java")
    ]
    manager = Manager(
        "Adam", "Smith", "example@you.com", 1000.50, employees_list
    )
    assert manager.employees == employees_list


def test_manager_set_employees_standard():
    employees_list = [
        Employee("John", "Wayne", "john@wayne.com"),
        Software_Developer("Steve", "Norman",
                           "setve@norman.com", 1000.50, "javascript")
    ]
    new_employees_list = [
        Employee("Gary", "Richards", "gary@richards.com"),
        Mandate_Contract_Employee(
            "Alex", "Bellingham", "al@bellingham.com", 20, 20)
    ]
    manager = Manager(
        "Adam", "Smith", "example@you.com", 1000.50, employees_list
    )
    assert manager.employees == employees_list
    manager.set_employees(new_employees_list)
    assert manager.employees == new_employees_list


def test_manager_hire_an_employee_standard():
    employees_list = [
        Employee("John", "Wayne", "john@wayne.com"),
        Software_Developer("Steve", "Norman",
                           "setve@norman.com", 1000.50, "javascript")
    ]
    new_employee = Software_Developer(
        "Jack", "Jones", "j@j.com", 1000.50, "java")
    manager = Manager(
        "Adam", "Smith", "example@you.com", 1000.50, employees_list
    )
    assert manager.employees == employees_list
    manager.hire_an_employee(new_employee)
    employees_list.append(new_employee)
    assert manager.employees == employees_list


def test_manager_fire_an_employee_standard():
    employees_list = [
        Employee("John", "Wayne", "john@wayne.com"),
        Software_Developer("Steve", "Norman",
                           "setve@norman.com", 1000.50, "javascript")
    ]
    manager = Manager(
        "Adam", "Smith", "example@you.com", 1000.50, employees_list
    )
    employee_to_fire = employees_list[0]
    manager.fire_en_employee(employee_to_fire)
    employees_list.remove(employees_list[0])
    assert manager.employees == employees_list
