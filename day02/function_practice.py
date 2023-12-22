def eligible_to_vote(age, country):
    if age >= 18 and country.upper() == 'USA':
        print('You are eligible to vote!')
    else:
        print('You are not eligible to vote')


eligible_to_vote(18, 'USA')

print('-----------------------------------------')


# Create a function that can calculate the grade of the student based on the score:
def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid score"


print(calculate_grade(80))
# Example usage
# score = float(input("Enter the student's score:\n "))
# result = calculate_grade(score)
# print(f"The student's grade is: {result}")


print('-----------------------------------------')

"""
Create a function that can if the given integer is positive, negative or zero
"""


def number(value):
    if value > 0:
        return 'Positive'
    elif value < 0:
        return 'Negative'
    else:
        return 'Zero'


print(number(1))
# num = int(input("Enter an integer: \n"))
# result = number(num)
# print(f'The number is : {result}')

print('-----------------------------------------')


# Create a function that can check if a string is palindrome, the function
# should return true if the given string is palindrome.

def is_palindrome(string):
    # Remove any spaces or punctuation from the string
    string = ''.join(string.split()).lower()
    # Reverse the string
    reversed_string = string[:: -1]
    # Compare the string with its reverse
    if string == reversed_string:
        # Return True if they are equal
        return True
    else:
        # Return False if they are not equal
        return False


print(is_palindrome('Madam'))

print('-----------------------------------------')

"""
Write a program that asks user to enter
 number for 5 times, and print how many positive and negative numbers user entered
"""


def count():
    positive_num = 0
    negative_num = 0

    for _ in range(5):
        value = float(input("Enter an number: \n"))
        if value > 0:
            positive_num += 1
        elif value < 0:
            negative_num += 1
    print(f"{positive_num} positive and {negative_num} negative")


count()
