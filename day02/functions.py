# Methods must be created in the Class
# Function can not be created in the Class in Python
# Both function and Methods are used to grouping a series of code fragment to perform a task
import numbers


def display_message():
    print('Hello World')
    print("Hello Chicago")
display_message() # call the function

print('-------return function------------')

def value():
    return 'Python Programming'
print(value())

print('-------return function a value----')

def return_int() -> int: # we use Lambda expresion
    return 10
print(return_int())

print('-------function with parameters----')
def divide(num1,num2):
    return num1/num2
print(divide(10,2))

def square(num: int):
    return num * num
print(square(10))

def add(num1, num2) -> int:
    return num1 + num2
print(add(10,20))

def add1(num3,num4) -> numbers: # USE (numbers) if we want to add,multiply,devide double or int or float
    return num3*num4
print(add1(120.23,12))








