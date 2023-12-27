"""
Write a program that can return the factorial number of any given number
"""

print('--------factorial--------------------')


def factorial_number(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


print(factorial_number(7))

print('-----------------------------------')


def characters(s):
    letters = []
    digits = []
    special_chars = []

    for char in s:
        if char.isdigit():
            digits += char
        elif char.isalpha():
            letters += char
        else:
            special_chars += char

    print("The digits in the string are:", digits)
    print("The letters in the string are:", letters)
    print("The special characters in the string are:", special_chars)
    return letters, digits, special_chars


print(characters('mn@#123Ab!'))

print('-----------------------------------')
"""
Create a python file named sum_of_digits, Write a program that can return the sum of digits from a  string
"""


def sum_of_digits(value):
    sum_digits = 0
    for c in value:
        if c.isdigit():
            sum_digits += int(c)
    return sum_digits


print(sum_of_digits('A1B2C3'))

print('-----------------------------------')

"""
Create a python file named finra, Write a program which prints out the numbers from 1 to 100 but for numbers which 
are a multiple of both 3 and 5, print "FINRA" instead of the number,for numbers which are a multiple of 3,
print "FIN" instead of the number and for numbers which are a multiple of 5, print "RA" instead of the number.
  
"""


def finra():
    result_list = ''
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result_list += "FINRA"
        elif num % 3 == 0:
            result_list += "FIN"
        elif num % 5 == 0:
            result_list += "RA"
        else:
            result_list += (str(num))

    return result_list


result = finra()
output_String = " ".join(result)
print(output_String)

print('-----------------------------------')


# grade_calculator

def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score <= 59:
        return "F"
    else:
        return "Invalid Entry"


def get_user_input():
    while True:
        try:
            user_score = float(input("Enter your score:\n "))
            return user_score
        except ValueError:
            print("Invalid Entry. Please enter a valid numeric score.")


def get_user_decision():
    while True:
        decision = input("Would you like to continue? (yes/no): \n ").lower()
        if decision in ["yes", "no"]:
            return decision
        else:
            print("Invalid Entry. Please enter 'yes' or 'no'.")


# Main program
while True:
    user_score = get_user_input()
    grade = calculate_grade(user_score)
    print(f"Your grade is: {grade}")

    decision = get_user_decision()
    if decision == "no":
        print("Thank you for using Cydeo Grade Calculator APP")
        break
