 # arithmetic: +, - , *, /, %

print(10 - 2)

print(10 + 2)

print(10 * 3)

print(100 / 2)  # in Python division we will get Float Nr always

print(int(100 / 2)) # but if we want int then we need casting: (int) as it is showing in example

print(10 % 2)

# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100

a = 200

print(a)


a += 100

print(a)

a -= 50

print(a)

a /= 2

print(a)


# logical operators: and, or, not
s = 'Hello World'

print('H' and 'W' in s) # verify if element H and W contains in String

print(True and True)
print(True or False)

s = 'Java Python C# C++'

print('Java' or 'Ruby' in s) # check if Java is presenting in the String

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'

print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains()
print('Python' not in s)

print(not False)
print(not True)  # !

print('----------------------------------')

s = 'Java'
s2 = 'Java'

print( s is s2) # to heck if two variables are referencing to the same objects ( == operator of java)