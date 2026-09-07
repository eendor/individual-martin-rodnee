from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self, food):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__()
        self._name = name
        self._breed = breed
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def eat(self, food):
        print(f"Eaten {food}")

    def make_sound(self):
        print("Bark! Woof! Arf!")

    def call(self):
        print(f"Here {self._name}!")

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__()
        self._name = name
        self._breed = breed
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def eat(self, food):
        print(f"Serve me {food}")

    def make_sound(self):
        print("Miaow! Nyaw! Nyaaaaa!")

    def call(self):
        print(f"{self._name}, come on!")

dog1 = Dog("Isis", "Dalmatian", 15)
dog1.eat("Steak")
dog1.make_sound()
dog1.call()

cat1 = Cat("Puss", "Persian", 4)
cat1.eat("Tuna")
cat1.make_sound()
cat1.call()
