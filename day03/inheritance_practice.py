"""
Create a python file named inheritance_practice:
Create an abstract class named Animal:
Variables:
name, breed(final), gender(final),  age, size, color(final)

Encapsulate all the fields

Add a constructor that can set all the fields

Methods:
eat() ==> different animals eat different foods
drink() ==> all the animals drink water
toString() ==> to display the full info of the animal


Create the following subclasses of Animal:
Dog
eat(): Dog Food

Cat
eat(): Cat Food

Parrot
eat():
Eagle
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, breed, gender, age, size, color):
        self.__name = name
        self.__breed = breed
        self.__gender = gender
        self.__age = age
        self.__size = size
        self.__color = color

    def __str__(self):
        return f"Name: {self.__name}, Breed: {self.__breed}, Gender: {self.__gender}, " \
               f"Age: {self.__age}, Size: {self.__size}, Color: {self.__color}"

    @abstractmethod
    def eat(self):
        pass

    def drink(self):
        return "All animals drink water"


class Dog(Animal):
    def __init__(self, name, gender, age, size, color):
        super().__init__(name, "Dog Breed", gender, age, size, color)

    def eat(self):
        return "Dog food"


class Cat(Animal):
    def __init__(self, name, gender, age, size, color):
        super().__init__(name, "Cat Breed", gender, age, size, color)

    def eat(self):
        return "Cat food"


class Parrot(Animal):
    def __init__(self, name, gender, age, size, color):
        super().__init__(name, "Parrot Breed", gender, age, size, color)

    def eat(self):
        return "Parrot food"


class Eagle(Animal):
    def __init__(self, name, gender, age, size, color):
        super().__init__(name, "Eagle Breed", gender, age, size, color)

    def eat(self):
        return "Eagle food"


# Example usage
dog = Dog("Ciuc", "Male", 3, "Medium", "Brown")
print(dog)
print(dog.eat())
print(dog.drink())

cat = Cat("Mila", "Female", 2, "Small", "Gray")
print(cat)
print(cat.eat())
print(cat.drink())

parrot = Parrot("Polly", "Female", 1, "Small", "Green")
print(parrot)
print(parrot.eat())
print(parrot.drink())

eagle = Eagle("Tigan", "Male", 5, "Large", "Brown")
print(eagle)
print(eagle.eat())
print(eagle.drink())
