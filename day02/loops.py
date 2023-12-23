s = 'Python'

for each in s:  # s means sequence
    print(each)

print('---print index number--')

for i in range(0, len(s)):
    print(i)  # access the index nr
#  print(s[i])  # to access each character

print('---reverse index numb----')

for i in range(-len(s), 0):
    print(i)  # reverse
# print(s[i])

print('----reverse the string----')

for i in reversed(range(0, len(s))):
    print(s[i])  # reverse str
#   print(i) reverse index nr

print('----reverse version of the string--')

result = ''

for x in s[::-1]:
    result += x

print(result)

print('-----Loop------------------')

for x in range(1, 6):
    print('Hello World')

print('-------While Loop----------------')

num = int(input('Enter a positive number:\n'))

while num <= 0:
    num = int(input('Enter a positive number:\n'))

print(f'You have entered {num}')

print('------While-----------------')

answer = input('Enter yes or no:\n')

while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('Enter yes or no:\n')

print(f'You have entered {answer}')
