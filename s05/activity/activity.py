from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def get_fullname(self):
        pass

    @abstractmethod
    def add_request(self):
        pass

    @abstractmethod
    def check_request(self):
        pass

    @abstractmethod
    def add_user(self):
        pass


class Employee(Person):
    def __init__(self, first_name, last_name, email, department):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__department = department

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_fullname(self):
        return f"{self.__first_name} {self.__last_name}"

    def add_request(self):
        return "Request has been added"

    def check_request(self):
        pass

    def add_user(self):
        pass

    def login(self):
        return f"{self.__email} has logged in"

    def logout(self):
        return f"{self.__email} has logged out"


class TeamLead(Person):
    def __init__(self, first_name, last_name, email, department):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__department = department
        self.__members = []

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_members(self):
        return self.__members

    def set_members(self, members):
        self.__members = list(members)

    def get_fullname(self):
        return f"{self.__first_name} {self.__last_name}"

    def add_request(self):
        pass

    def check_request(self):
        return "Request has been checked"

    def add_user(self):
        pass

    def login(self):
        return f"{self.__email} has logged in"

    def logout(self):
        return f"{self.__email} has logged out"

    def add_member(self, employee):
        self.__members.append(employee)


class Admin(Person):
    def __init__(self, first_name, last_name, email, department):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__department = department

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_fullname(self):
        return f"{self.__first_name} {self.__last_name}"

    def add_request(self):
        pass

    def check_request(self):
        pass

    def add_user(self):
        return "User has been added"

    def login(self):
        return f"{self.__email} has logged in"

    def logout(self):
        return f"{self.__email} has logged out"


class Request:
    def __init__(self, name, requester, date_requested, status="pending"):
        self.__name = name
        self.__requester = requester
        self.__date_requested = date_requested
        self.__status = status

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_requester(self):
        return self.__requester

    def set_requester(self, requester):
        self.__requester = requester

    def get_date_requested(self):
        return self.__date_requested

    def set_date_requested(self, date_requested):
        self.__date_requested = date_requested

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def update_request(self):
        self.__status = "updated"
        return f"Request {self.__name} has been updated"

    def close_request(self):
        self.__status = "closed"
        return f"Request {self.__name} has been closed"

    def cancel_request(self):
        self.__status = "cancelled"
        return f"Request {self.__name} has been cancelled"


if __name__ == "__main__":
    # Test cases from the capstone instructions.
    employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
    employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
    employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
    employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")
    admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
    teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
    req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
    req2 = Request("Laptop repair", employee1, "1-Jul-2021")

    assert employee1.get_fullname() == "John Doe", "Full name should be John Doe"
    assert admin1.get_fullname() == "Monika Justin", "Full name should be Monika Justin"
    assert teamLead1.get_fullname() == "Michael Specter", "Full name should be Michael Specter"
    assert employee2.login() == "sjane@mail.com has logged in"
    assert employee2.add_request() == "Request has been added"
    assert employee2.logout() == "sjane@mail.com has logged out"

    teamLead1.add_member(employee3)
    teamLead1.add_member(employee4)
    for indiv_emp in teamLead1.get_members():
        print(indiv_emp.get_fullname())

    assert admin1.add_user() == "User has been added"

    req2.set_status("closed")
    print(req2.close_request())
