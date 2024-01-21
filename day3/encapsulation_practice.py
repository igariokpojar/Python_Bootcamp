"""
Create a python file named encapsulation_practice:
create a class called Item
private variables:
name, unit_price, quantity

Encapsulate all the fields:
Conditions:
name can not be empty
unit price can not be negative
quantity can not be negative

If invalid data are given to set the filed, then make sure to throw an error during the runtime.
hint: you can use 'raise RuntimeError('Exception message')

Add a constructor that allows user to set all the fields when the object is created.
(If the arguments not valid it should not be set to the instances)

Methods:
calcCost(): returns the total cost
toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()
"""


class Item:
    def __init__(self, name, unit_price, quantity):
        self.__set_name(name)
        self.__set_unit_price(unit_price)
        self.__set_quantity(quantity)

    def __set_name(self, name: str):
        if type(name) != str:
            raise RuntimeError('f Name cannot be empty.')
        if name == '':
            raise RuntimeError('f Name can not be empty')

        self.__name = name

    def __set_unit_price(self, unit_price):
        if unit_price < 0:
            raise RuntimeError("Unit price cannot be negative.")
        self.__unit_price = unit_price

    def __set_quantity(self, quantity):
        if quantity < 0:
            raise RuntimeError("Quantity cannot be negative.")
        self.__quantity = quantity

    def calc_cost(self):
        return self.__unit_price * self.__quantity

    def __str__(self):
        return f"Name: {self.__name}, Unit Price: ${self.__unit_price:.2f}, " \
               f"Quantity: {self.__quantity}, Total Cost: ${self.calc_cost():.2f}"


item1 = Item('Samsung', 1256, 12)
print(item1)
