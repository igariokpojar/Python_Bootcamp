days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 1, 2, 3, 4, 5, 6, 7, True, False)
# tuple could contain the multiple elements, size is fixed -> size can not be increase or decrease

print(type(days))
print(len(days))

print(days)

# days[0] = 'Java'
# print(days)


print(days[0])  # access the elements of tuple
print(days[-1])

days = ('Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# work_days = days[1:-3]
work_days = days[1:4]  # slices elements from index 1 to 4 ( index 4 is excluded)
print(work_days)

week_days = days[:-2]  # slices from begin exclude last 2 elements
print(week_days)

weekend = days[-3:]  # slices backward from end
print(weekend)

# == ,  is
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)


print(tuple1 == tuple2)
print(tuple1 is tuple2)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 5
print(tuple4)

reversed_tuple1 = days[::-1]  # reverse tuple

print(reversed_tuple1)

reversed_tuple2 = tuple(reversed(days))

print(reversed_tuple2)  # reverse Method it's used to revers tuple

print(days.index('Wednesday'))

numbers = (10, 10, 10, 10, 20, 30, 40, 50, 10)

print(numbers.count(10))

print('------use topple with loop-------------------')

for x in days:
    print(x)

print('------access the index of tuple---------------')

for x in range(0, len(days)):
    print(x)


print('------iterate in reverse order--------------')

for x in reversed(range(0, len(days))):
    print(x)


print('----nested tuple---------------------')

nested_tuple = ((1, 2, 3), (4, 5, 6, 7, 8), (9, 10))
# multi dimensional array in Java

print(len(nested_tuple))

print('------iterate nested tuple-------------------')

for x in nested_tuple:
    print(x)  # x represent each tuple that we have
    for y in x:
        print(y)

print('-----access if index of tuple--------------')

for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])
