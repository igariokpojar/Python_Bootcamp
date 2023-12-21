"""

Ask the user to enter the following info, and diplsay the user entered info:
                        name (String)
                        age (integer)
                        gender (String)
                        company (String)
                        job title (String)
                        salary (float)

            Ex:
                Given Data:
                    name = "Daniel"
                    age = 28
                    gender = 'Male'
                    company_name = 'Google Inc'
                    job_title = "Scrum Master"
                    salary = 90000


                Output:
                    Daniel is 28 years old, gender is Male
                    Daniel works at Google Inc as a Scrum Master
                    Daniel makes $ 90000 per year
"""
name = "Daniel"
age = 28
gender = 'Male'
company_name = 'Google Inc'
job_title = "Scrum Master"
salary = int(90000)
print(f'{name} is {age} years old, gender is {gender}')
print(f'{name} works at {company_name} as a {job_title}')
print(f'{name} makes $ {salary} per year')

print('-------------------------------------------')
"""
 1.1 Ask the user to enter the following info:
                     1.1.1 "Enter your name"
                     1.1.2 "Enter your hourly rate"
                     1.1.3 "How many hours you work in a week?"

            1.2 write a program that can can culate the salary based on the user given info
                         Hint: number of weeks are 52
                         
                         salary = hourlyRate * weeklyHour * 52

            Ex:
                Given Data:
                    name = Joshua
                    hourly_rate = 40
                    weekly_hours = 45
                    
                    
                Output:
                    Hello Joshua, your salary is $ 93600.00

name = input("Enter your name:\n")
hourly_rate = input("Enter your hourly rate:\n")
weekly_hours = input("How many hours you work in a week?:\n")
number_of_weeks = 52
salary1 = float(hourly_rate) * float(weekly_hours) * number_of_weeks
#print(f'Hello {name}, your salary is {salary1} ')
print(f"Hello {name}, your salary is $ {salary:.2f}")
"""
"""
grade_level = int(input("Enter your grade level number: \n"))
if 1 <= grade_level <= 5:
    school = 'Elementary school'
elif 6 <= grade_level <= 8:
    school = 'Middle school'
elif 9 <= grade_level <= 12:
    school = 'High school'
elif 13 <= grade_level <= 16:
    school = 'College'
elif 17 <= grade_level <= 18:
    school = 'Grad School'
print(f"You are in {school}.")
print('-------------------------------------------')
grade_level = int(input("Enter your grade level number: \n"))
if 1 <= grade_level <= 5:
    school = 'Elementary school'
elif 6 <= grade_level <= 8:
    school = 'Middle school'
elif 9 <= grade_level <= 12:
    school = 'High school'
elif 13 <= grade_level <= 16:
    school = 'College'
elif 17 <= grade_level <= 18:
    school = 'Grad School'
else:
    school = 'Invalid grade level given'
print(school)
"""
"""number = int(input("Enter your number: \n"))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Entered number is nod divided by 3 or 5')
"""
"""
grade = str(input("Enter your grade: \n"))
if grade == 'A':
    message = 'Excellent'
elif grade == 'B':
    message = 'Great Job'
elif grade == 'C':
    message = 'Good'
elif grade == 'D':
    message = 'Passed'
elif grade == 'F':
    message = "Fail"
else:
    message = 'invalid entry'
print(message)"
"""
"""
age = int(input('Enter  your the age:\n'))
if age < 0 or age > 150:
    age_group = "Invalid"
elif age < 21:
    age_group = "Teenager"
elif age < 55:
    age_group = "Adult"
elif 55 < age <= 150:
    age_group = "Senior"
# Print the result using a single print statement
print(age_group)
"""

print('-------------------------------------------')

# Ask the user to enter a number
user_number = int(input("Enter a number (0-9): "))

# Convert the number to words using a ternary operator
number_in_words = (
    "Zero" if user_number == 0 else
    "One" if user_number == 1 else
    "Two" if user_number == 2 else
    "Three" if user_number == 3 else
    "Four" if user_number == 4 else
    "Five" if user_number == 5 else
    "Six" if user_number == 6 else
    "Seven" if user_number == 7 else
    "Eight" if user_number == 8 else
    "Nine" if user_number == 9 else
    "Invalid")
# Print the result
print(number_in_words)






















