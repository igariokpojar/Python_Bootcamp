name = 'Alla'
age = 35
gender = 'F'
company = 'Trans Quality'
jobTitle = 'Software Engineer'
yearsOfExperience = 2
salary = 105000
is_fullTime = True
is_married = True
employee_id = True

print('--------------------------')
"""
2. create a python file named FlightTicket, and declare the following variables:
                1. from
                2. to
                3. ticketPrice

    use concatenation to display the full info of the ticket
    
    ex:
            Given Data:
                from = "Las Vegas"
                to = "McLean"
                ticket_price = 425.5

            Output:
                From Las Vegas to McLean is $425.5
"""

From = "Las Vegas"
to = 'McLean'
ticketPrice = 425.5
print(f'From {From} to {to} is {ticketPrice}')

print('--------------------------')
"""

3. Create a python file named ShippingAddress. Declare the following variables:
                    name
                    building_number
                    street_name
                    city
                    state
                    zip_code

    Use concatenation to print the full shipping address

        Ex:
            Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""
Name = "Aaron Kissinger"
building_number = '13621A'
street_name = 'Legacy Circle'
city = 'Saint Charles'
state = 'Il'
zip_code = 60177

print(f'{Name}\n{building_number} {street_name}\n{city} {state} {zip_code}')

print('--------------------------')
"""
Given Data:
                    side = 5

                output:
                    Area of the square is equal to 25
                    Perimeter of square is equal to 20
"""
side = 5
area = side ** 2
perimeter = side * 4
print(f'Area of the square is equal to {area}')
print(f'Perimeter of square is equal to {perimeter}')

print('--------------------------')
"""
Ex:
                Given Data:
                    length = 5
                    width = 2

                output:
                    Area of the rectangle is equal to 10
                    Perimeter of rectangle is equal to 20
"""
length = 5
width = 2
area1 = length * width
perimeter1 = 2 * (length + width)
print('Area of the rectangle is equal to ', area1)
print('Perimeter of rectangle is equal to', perimeter1)

print('--------------------------')
"""
Ex:
                Given data:
                    kg = 100

                output:
                    100 kg is equal to 220 pounds
"""


# Define a function to convert kilograms to pounds
def kg_to_pounds(kg):
    # 1 kg is equal to 2.20462262185 pounds
    return kg * int(2.2)


# Given data
kg = 100

# Call the function and print the output
output = kg_to_pounds(kg)
print(f"{kg} kg is equal to {output} pounds")

print('--------------------------')
"""
Given Data:
                     gallon = 10

                output:
                    10 gallon is equal to 37.9 litters
"""
gallon = 10
def gl_to_litters():
    return gallon * 3.79
print(f'{gallon} gallons is equal to {gl_to_litters()} litters')

print('--------------------------')
"""
use string concatenation to display the phone number
            ex:
                if  country_code = 1
                    area_code = 703
                    localNumber = 4512625

                output:
                    Your phone number is +1(703)-4512625
"""
countryCode = 1
areaCode = 703
localNumber = 4512625
print(f'Your phone nuber is +{countryCode}({areaCode})-{localNumber}')

print('--------------------------')
"""
use concatenation to display the birthday of the person

                 if  name = "John"
                     birth_day = 25
                     birth_month = "April"
                     birth_year = 1995;

                 output:
                     John was born on April/25/1995.
"""
name1 = 'Alex'
birth_day = 15
birth_month = "April"
birth_year = 2016
print(f'Alex was born on {birth_month}/{birth_day}/{birth_year}')

print('--------------------------')
"""
 Ask the user to enter the following info, and display the shipping address of the user:
                    1. "Enter your full name"
                     2. "Enter your building number"
                     3. "Enter your street name"
                     4. "Enter your city name"
                     5. "Enter your state name"
                     6. "enter your zip code"

             Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping address is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""
name2 = input("Enter your full name:\n")
building_number2 = input("Enter your building number:\n")
street_name2 = input("Enter your street name:\n")
city = input("Enter your city name:\n")
state = input("Enter your state name:\n")
zipcode = input("enter your zip code:\n")
print("Your shipping address is:")
print("\t" + name2)
print("\t" + building_number2 + " " + street_name2)
print("\t" + city + ", " + state + " " + zipcode)


