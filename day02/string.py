name = 'Python'

print(len(name))
print(name[0]) # access the first element
print(name[len(name) - 1]) # access the last index number

print('---------------------------------------')

print(name[-1]) # access the last index number by reversing
print(name[-2]) # access the second index number by reversing

print('-------------slise method--------------')

s = 'Java Programming Language'
s2 = s[5:16] # Slise method same as in Java Substring method
print(s2)

s3 = s[:4] # slicing  form index 0 to 4
print(s3)

print('------------- reverse slicing------------')

s4 = s[::-1]  # reverses the string after slicing

print(s4)

s = 'Python Programming'

s5 = str(reversed(s))

print(type(s5))
reversed(s5)
print(s5)
s5 = s[::-1]
print(s5)

s5 = 'python Programming'

s6 = s5[7:]  # by default, it slices the string from index 7 to the end including the last character

print(s6)

s7 = 'CYDEO SCHOOL'
# str(reversed(s7))

print('---------String Methods----------------')
# print( help(str))

s = 'python programming language'

s = s.capitalize()  # CAPITALIZE the first character
s = s.title()  # capitalize each word in the String
print(s)

s = "            Python           "
s = s.strip()  # trim method of java return String without white spaces
print(s)

s = 'JAVA'
print(s.index('A'))
print(s.rindex('A'))  # works as last_index method in Java

s = 'Java Java'

s = s.replace('Java', 'Python', 1)  # replace method returns new String at the End so assign to new Variable
print(s)

s = 'C# C# Python'
s = s.replace(' C#', ' Java')
print(s)

s = 'Java jAVA java JAVA Python Python'
count_java = s.lower().count('java')  # count method help us to get the frequency of specific word or element
count_python = s.count('Python')
print(count_java)
print(count_python)

s1 = 'java'
s2 = 'JAVA'
print(s1.lower() == s2.lower())  # ignore case, compare two Strings

s = 'Java'
print(s[0].islower())  # check if the first (or any) character from String is lower case
print(s[0].isupper())  # check if the first (or any)  character from String is upper case

s = 'a'
print(s.isalpha())  # check if characters are alphabetically

s = '1'
print(s.isdigit())  # check if characters are numeric

s = 'Cydeo School'
print(s.istitle())

































