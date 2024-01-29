from typing import final  # in order to use Final Keyword we need to import TYPING module and final

pi: final = 3.14  # pi is a constant

pi = 3.5


@final  # declare final Class
class Animal:
    pass


class Dog(Animal):  # Animal is marked as final Class and should not be a subclass
    pass


class Employee:

    @final  # final can be used for methods
    def work(self):
        print('Working')


class Driver(Employee):

    def work(self):
        print('Driving')


class Person:  # ARCHIVED THE CONSTANT

    def __init__(self, age: int):
        self.__age = age

    @property  # getter
    def person_age(self):
        return self.__age

    @person_age.setter  # setter
    def person_age(self, value):
        raise RuntimeError(f' age is constant, can not be changed')


person1 = Person(10)

print(person1.person_age)

# person1.person_age = 100

print(person1.person_age)

print(person1.__age)  # it has attributes but is private
