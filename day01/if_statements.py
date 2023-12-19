
if False :
    print('Python Programming')

print('Java Programing')

print('------------if statement------------')

score = 70
if score >= 60:
    print('Congrats! you pass the exam')

    s = 'Hello World'
    if 'H' and 'W' in s:
        print(s, 'has', 'H and W')

print('-----------if else statement------')

if score >= 60:
    print('Pass')
else:
    print('Fail')

print('---------------------------------')
age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = "Not Eligible"

print(result)

print('---------------------------------')

# Ternary:

age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible' # this is ternary in java, is shor cut

print(result)

print('------Multi branch if----------------')

num = 100

result = None

if num > 0:
    result = "Positive"
elif num < 0:  # same with else if block of Java
    result = "Negative"
else:
    result = "Zero"

print(result)

print('--------ternary operations----------')

num = 200

result2 = 'Positive' if num >= 0 else 'Zero'

print(result2)

print('--------nested-if---------------')

score = -330

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')

print('-------nested-if--------------')

score = 95

if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('Invalid Score')


"""
A score of a student is given, write a program that can calculate the grade of the student

    Possible grades are:
        1. A ( 90 ~ 100)
        2. B ( 80 ~ 90 )
        3. C ( 70 ~ 80 )
        4. D ( 60 ~ 70 )
        5. F ( less than 60)
"""