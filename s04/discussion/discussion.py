# Classes
# Classes serve as blueprints for creating objects. Each object has characteristics (properties) and behaviors(methods).

# Class - blueprint
# Object - Instance created from a class
# Properties 
# Methods

class Car():
	# Properties
	# __init__ method is called automatically whenver a new Car object is created
	# It is used to initialize(assign) the object's properties
	# The first parameter, "self", refers to the current object being created
	# The remaining parameters are values provided when creating the object
	def __init__(self, brand, model, year_of_make):
		# Assign the values passed by the user to the object's properties
		self.brand = brand
		self.model = model
		self.year_of_make = year_of_make

		# Properties with default values
		self.fuel = "Gasoline"
		self.fuel_level = 100

	# Methods
	def drive(self, distance):
		print(f"The car has driven {distance} kilometers.")
		print(f"The fuel level left: {self.fuel_level - distance}")


new_car = Car("Nissan", "GT-R", "2019")

print(f"My car is a {new_car.brand} {new_car.model}.")

new_car.drive(75)

# 4 Pillars of OOP
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

# ENCAPSULATION
class Person():
	def __init__(self):
		self._name = "John Doe"
		self._age = 0

	def set_name(self, name):
		self._name = name

	def get_name(self):
		print(f"Name of Person: {self._name}")

	def set_age(self, age):
		self._age = age

	def get_age(self):
		print(f"Age of Person: {self._age}")


# Create a Person object
p1 = Person()
# print(p1._name)
p1.get_name()
p1.set_name("Bob Doe")
p1.get_name()


# Inheritance
# Parent Class - The class whose properties and methods are inherited
# Child Class - The class that inherits from the parent class

# Syntax:
# class childClassName(ParentClassName)

class Employee(Person):
	def __init__(self, employeeId):
		super().__init__()
		self._employeeId = employeeId

	def get_employeeId(self):
		print("The employee ID is {self._employeeId}")

	def set_employeeId(self, employeeId):
		self._employeeId = employeeId

	def get_details(self):
		print(f"{self._employeeId} belongs to {self._name}")

emp1 = Employee("Emp-001")
emp1.get_details()

emp1.set_name("Juan Dela Cruz")
emp1.set_age(18)
emp1.get_details()

# Polymorphism
class Zuitt():
	def tracks(self):
		print("We are currently offering 3 tracks (Developer Career, Pi-Shaped Career and Short Courses).")
	
	def num_of_hours(self):
		print("Learn web development in 360 hours.")

class DeveloperCareer(Zuitt):
	def num_of_hours(self):
		print("Learn web development in 240 hours.")

class PiShapedCareer(Zuitt):
	def num_of_hours(self):
		print("Learn web development in 140 hours.")


course1 = DeveloperCareer()
course2 = PiShapedCareer()

course1.num_of_hours()
course2.num_of_hours()

# Abstraction
# Abstraction hides the implementation details and exposes only the essential functionality to the user

# Abstract Class
# abc - is a built-in Python module that provides tools for creaing abstract classes and abstract methods
# ABC - is a base class used to define an abstract class
# abstractmethod - is a method with no implementation that every child class must implement

from abc import ABC, abstractmethod

class Polygon(ABC):
	@abstractmethod
	def printNumberOfSides(self):
		# "pass" indicates that no implementation is provided
		pass


class Triangle(Polygon):
	def __init__(self):
		super().__init__()

	def printNumberOfSides(self):
		print("This polygon has 3 sides.")

class Pentagon(Polygon):
	def __init__(self):
		super().__init__()

	def printNumberOfSides(self):
		print("This polygon has 5 sides.")

shape1 = Triangle()
shape1.printNumberOfSides()
shape2 = Pentagon()
shape2.printNumberOfSides()