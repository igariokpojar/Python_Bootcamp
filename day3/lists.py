
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


