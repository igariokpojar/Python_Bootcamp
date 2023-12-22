# Methods must be created in the Class
# Function can not be created in the Class in Python
# Both function and Methods are used to grouping a series of code fragment to perform a task
import numbers


def display_message():
    print('Hello World')
    print("Hello Chicago")


display_message()  # call the function

print('-------return function------------')


def value():
    return 'Python Programming'


print(value())

print('-------return function a value----')


def return_int() -> int:  # we use Lambda expresion
    return 10


print(return_int())

print('-------function with parameters----')


def divide(num1, num2):
    return num1 / num2


print(divide(10, 2))


def square(num: int):
    return num * num


print(square(10))


def add(num1, num2) -> int:
    return num1 + num2


print(add(10, 20))


def add1(num3, num4) -> numbers:  # USE (numbers) if we want to add,multiply,devide double or int or float
    return num3 * num4


print(add1(120.23, 12))

print('-------function with multiple arguments----')


def calculate(num1, num2, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))

print(calculate(100.5, 2.5, '/'))

print('---example of method overloading--------------')


def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    # 3rd and 4th parameters they do have by default 0 is means tha is NOT Must give the parameter for last 2 param
    return n1 + n2 + n3 + n4


print(sum(10, 20))

print(sum(10, 20, 30))

print(sum(10, 20, 30, 40))

print('--------Custom Function----------------')


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())  # strip method for cut white space


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)


"""
1. Declaring
2. parameters
3. restricting parameter' data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing -> means tha any data can be assigned to to the parameters
"""
