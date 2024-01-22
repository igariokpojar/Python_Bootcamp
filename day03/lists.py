groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')  # append means add
groceries_list.extend(('Beef', 'Oranges', 'Onions '))  # EXTEND Method

print(len(groceries_list))
print(groceries_list)

print('----------------------------------------------')

groceries_list[-2] = 'Cherry'  # ORANGES UPDATED TO CHERRY
print(groceries_list)

groceries_list[-2:] = 'Cherry'  # it will print each character or Cherry
print(groceries_list)

print('---------update multiple elements------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)

numbers_list[2:-2] = [300, 4000, 5, 60000]

print(numbers_list)

print('---------slicing---------------------------')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2: -3]
print(list1)

list2 = characters[:4]
print(list2)

list3 = characters[2:]
print(list3)

characters[2:6] = ['C', 'D', 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']  # update or shifting elements in List

print(characters)

print('---------iterate list---------------------------')

names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)

names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)

print('-------update elements of list----------------')

nums = [10, 20, 30, 40, 50, 60]

for i in range(len(nums)):
    nums[i] = int(nums[i] / 2)  # iterate elements and divided by 2

print(nums)

print('---------iterate backwards-----------------')

nums = [10, 20, 30, 40, 50, 60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('---------iterate elements backward---------')

for x in nums[::-1]:
    print(x)

print('-------reverse method-------------')

for x in reversed(nums):
    print(x)

print('--------using while loop--------------')
i = 0

while i < len(nums):  # While loops are not recommend for List Data Structure
    print(nums[i])
    i += 1

print('------------------------------------')

for i in range(1, 6):
    i += 2
    print(i)

print('----------sort method-----------------')

nums = [60, 500, 10, 20, 15, 5, 0]

# nums.sort()  # ascending order

nums.sort(reverse=True)  # sorting in descender order (reverse)

print(nums)

print('--------reverse method---------------')

list1 = [10, 20, 30, 40]

# list1 = list( reversed(list1) )

list1.reverse()

print(list1)

print('-------convert list to tuple--------')

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
list_elements.append('SWIFT')

print(list_elements)  # list elements

tuple_elements = tuple(list_elements)

print(tuple_elements)  # tuple elements

print('---------equal method----------------')

list1 = [1, 2, 3, 4, 5]  # list is changeable and we have FALSE
list2 = [1, 2, 3, 4, 5]

print(list1 is list2)

tuple1 = (1, 2, 3, 4, 5)  # tuple are fixed and we got TRUE
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 is tuple2)

print('---------remove method---------------')

groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(groceries_list)

groceries_list.remove('Beef')

print(groceries_list)

groceries_list.pop()  # means last in first out or (remove the element)

print(groceries_list)

groceries_list.pop(1)  # remove element with index 1

print(groceries_list)

groceries_list.insert(2, 'Apple')  # insert different element

print(groceries_list)

print(groceries_list.index('Eggs'))

nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]

print(nums.count(1))

