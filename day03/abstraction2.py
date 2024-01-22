import math
import numbers

from abc import ABC, abstractmethod  # import a class that is present on other module

# import abc

"""
abc: module name (built in Python Library module)
ABC: Abstract class in abc module
abstractmethod: annotations that can be given to abstract methods
this is traditional and recommend way to achieve Abstraction
"""


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):  # by Inherited ABC clas we achieved Abstraction

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):  # declare instances
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> numbers:
        return math.pow(self.radius) * math.pi


class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> numbers:
        return self.width * self.length


class Cube(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Cylinder(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


square1 = Square(5)

print(square1)
print(square1.area())