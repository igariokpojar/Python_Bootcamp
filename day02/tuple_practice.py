words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

"""
def palindrome(word):
    word = word.lower()
    reverse = word[:: -1]
    return word == reverse


for word in words:
    if palindrome(word):
        print(word)
"""


# tuples_practices.py

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]


def palindromes(words):
    palindrome_list = [word for word in words if is_palindrome(word)]
    for palindrome in palindrome_list:
        print(palindrome)


palindromes(words)

print('-----------------------------------------')

"""
Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

elements = set(list1) & set(list2)  # convert the lists to sets to easily find the intersection of elements

print('Common elements')
for e in elements:
    print(e)

print('--------------------------------------')
common = []
# loop through the first list
for element in list1:
    # check if the element is also in the second list
    if element in list2:
        # append the element to the common list
        common.append(element)

# display the common elements
print("The common elements are:")
for element in common:
    print(element)
print('------------------------------------------')
"""
Write a program that can count the even and odd number from a tuple of integers
                
                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers
"""

numbers = (1, 2, 3, 4, 5, 6, 7)

even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'There are {even} even numbers and {odd} odd numbers')



