"""
Write a program that can remove the duplicated elements from a list
Ex:
elements = [1,2,3,4,5,1,2,3,4,5]

Output:
[1, 2, 3, 4, 5]

Notes: Do Not use Set
"""


def remove_duplicates(input):
    unique_list = []
    for e in input:
        if e not in unique_list:
            unique_list.append(e)
    return unique_list


elements = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
output = remove_duplicates(elements)
print(output)

print("-----------------------------------------------")
"""
Write a program that can remove string elements from a list if the first and last characters of the string are same
ex:
list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}
output:
["Lan", "Ebrahim", "Farida"]

"""


def remove_strings_with_same_endpoints(input_list):
    result_list = [word for word in input_list if word[0] != word[-1]]
    return result_list


my_list = ["Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"]

output_list = remove_strings_with_same_endpoints(my_list)
print(output_list)


print('---------------------------------------------')


def remove_same_first_last_char(lst):
    return [w for w in lst if w[0] != w[-1]]


lst = ["Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"]
out = remove_same_first_last_char(lst)
print(out)

print('--------------------------------------------')

"""
Write a program that can display the unique elements of an arrayList:
ex:
list = [1, 1, 2, 3, 3, 4, 5, 5]
output:
[2, 4]
"""


def unique_elements(input_list):
    unique = [e for e in input_list if input_list.count(e) == 1]
    return unique


my_list = [1, 1, 2, 3, 3, 4, 5, 5]
my_result = unique_elements(my_list)
print(my_result)
