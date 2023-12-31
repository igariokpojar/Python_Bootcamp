"""
Write a program that can move all the zeros to the last indexes of ArrayList
Ex:
list: [1,0,2,0,3,0,4,0]

output:
[1, 2, 3, 4, 0, 0, 0, 0]
"""


def move_zeros_to_end(insert_list):
    # Count the number of zeros
    zero_count = insert_list.count(0)

    # Remove zeros from the list
    insert_list = [num for num in insert_list if num != 0]

    # Append zeros to the end
    input_list.extend([0] * zero_count)

    return input_list


# Example usage
input_list = [1, 0, 2, 0, 3, 0, 4, 0]
output_list = move_zeros_to_end(input_list)
print(output_list)

"""
write a program that can multiply each odd number by 2
ex: 
list = [1,2,3,4,5];

output: [2,2,6,4,10]

"""

print('-----------------------------------------')


def multiply_odd(add_list):
    odd_number = [x * 2 if x % 2 != 0 else x for x in add_list]
    return odd_number


add_list = [1, 2, 3, 4, 5]
out_put = multiply_odd(add_list)

print(out_put)

"""
Write a program that can remove all the names "Ahmed" from a list of strings
Ex:
list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

output:
["John", "Daniel", "James", "Muhammed"]
"""


def remove_word(list_words, name_to_remove):
    return [x for x in list_words if x != name_to_remove]


name_list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]
name_to_remove = 'Ahmed'
filtered_list = remove_word(name_list, name_to_remove)
print(filtered_list)

"""
Write a program that can display the palindrome strings from a list of String
Ex:
words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

output:
Anna
Level
"""

print('-----------------------------------------------')
def is_palindrome(word):
    return word.lower() == word.lower()[::-1]


def display_palindromes(words):
    palindrome_list = [word for word in words if is_palindrome(word)]
    for palindrome in palindrome_list:
        print(palindrome)


# Example usage
words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']
display_palindromes(words)

"""
Write a program that can display the common elements of two lists:
Ex:
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

Output:
4
5
"""
print('---------------------------------------------')


def common_elements(list1, list2):
    elements = set(list1) & set(list2)
    for e in elements:
        print(e)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements(list1, list2)
