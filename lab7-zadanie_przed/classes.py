class NegativeSalaryError(Exception):
    def __init__(self, salary):
        super().__init__("salary cannot be negative")
        self.__salary = salary


class NegativeWageError(Exception):
    def __init__(self, wage):
        super().__init__("wage cannot be negative")
        self.__wage = wage


class NegativeHrsError(Exception):
    def __init__(self, hours):
        super().__init__("hours cannot be negative")
        self.__hours = hours


class Employee():
    """
    Employee class. Contains attributes

    :param first_name: employee's first name
    :type first_name: str

    :param last_name: employee's last name
    :type last_name: str

    :param email: employee's email address
    :type email: str
    """

    def __init__(self, fname: str, lname: str, mail: str) -> None:
        """
        Creates an instance of the Employee class
        """
        self.__first_name = str(fname)
        self.__last_name = str(lname)
        self.__email = str(mail)

    @property
    def first_name(self) -> str:
        """
        Returns first name of an employee
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Returns last name of an employee
        """
        return self.__last_name

    @property
    def email(self) -> str:
        """
        Returns email of an employee
        """
        return self.__email

    def set_first_name(self, name: str) -> None:
        """
        Sets first name of the employee
        """
        self.__first_name = str.title(name)

    def set_last_name(self, name: str) -> None:
        """
        Sets last name of the employee
        """
        self.__last_name = str.title(name)

    def set_email(self, mail: str) -> None:
        """
        Sets email of the employee
        """
        self.__email = str(mail)


class Full_Time_Employee(Employee):
    """
    Full_Time_Employee class. Contains attributes

    :param first_name: employee's first name
    :type first_name: str

    :param last_name: employee's last name
    :type last_name: str

    :param email: employee's email address
    :type email: str

    :param salary: employee's salary in $
    :type salary: float

    """

    def __init__(self, fname: str, lname: str, mail: str, salary: float) -> None:
        """
        Creates an instance of the Full_Time_Employee class
        """
        super().__init__(fname, lname, mail)
        if (salary < 0):
            raise NegativeSalaryError(salary)
        self.__salary = float(salary)

    @property
    def salary(self) -> float:
        return self.__salary

    def set_salary(self, salary: float) -> None:
        if salary < 0:
            raise NegativeSalaryError(salary)
        else:
            self.__salary = float(salary)


class Mandate_Contract_Employee(Employee):
    """
    Mandate_Contract_Employee class. Contains attributes

    :param first_name: employee's first name
    :type first_name: str

    :param last_name: employee's last name
    :type last_name: str

    :param email: employee's email address
    :type email: str

    :param wage: employee's wage in $
    :type wage: float

    :param hours: employee's working hours in a month
    :type hours: float

    """

    def __init__(self, fname: str, lname: str, mail: str, wage: float, hrs: float) -> None:
        """
        Creates an instance of the Mandate_Contract_Employee class
        """
        super().__init__(fname, lname, mail)
        if (wage < 0):
            raise NegativeWageError(wage)
        self.__wage = float(wage)
        if (hrs < 0):
            raise NegativeHrsError(hrs)
        self.__hours = float(hrs)

    @property
    def wage(self) -> float:
        """
        Returns employee's wage
        """
        return self.__wage

    @property
    def hours(self) -> float:
        """
        Returns employee's working hours in a month
        """
        return self.__hours

    def set_wage(self, wage: float) -> None:
        if (wage < 0):
            raise NegativeWageError(wage)
        else:
            self.__wage = float(wage)

    def set_hours(self, hours: float) -> None:
        if (hours < 0):
            raise NegativeHrsError(hours)
        else:
            self.__hours = float(hours)

    def calculate_salary(self) -> float:
        return self.__hours * self.__wage


class Software_Developer(Full_Time_Employee):
    """
    Software_Developer class. Contains attributes

    :param first_name: employee's first name
    :type first_name: str

    :param last_name: employee's last name
    :type last_name: str

    :param email: employee's email address
    :type email: str

    :param salary: employee's salary in $
    :type salary: float

    :param language: employee's programming language
    :type language: str

    """

    def __init__(self, fname: str, lname: str, mail: str, salary: float, language: str) -> None:
        super().__init__(fname, lname, mail, salary)
        self.__language = language

    @property
    def language(self) -> str:
        return self.__language

    def set_language(self, language: str) -> None:
        self.__language = str(language)


class Manager(Full_Time_Employee):
    """
    Manager class. Contains attributes

    :param first_name: manager's first name
    :type first_name: str

    :param last_name: manager's last name
    :type last_name: str

    :param email: manager's email address
    :type email: str

    :param salary: manager's salary in $
    :type salary: float

    :param employees: list of employees
    :type employees: list[Employee]

    """

    def __init__(self, fname: str, lname: str, mail: str, salary: float, employees: list[Employee]) -> None:
        super().__init__(fname, lname, mail, salary)
        self.__employees = employees

    @property
    def employees(self) -> list[Employee]:
        return self.__employees

    def set_employees(self, employees: list[Employee]) -> None:
        self.__employees = employees

    def hire_an_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)

    def fire_en_employee(self, employee: Employee) -> None:
        self.__employees.remove(employee)
