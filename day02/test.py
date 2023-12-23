# import utility

from utility import sum, calculate  # similar to static import of java

result = sum(10, 20)

print(result)

result = calculate(10, 200, '+')

print(result)

import utility

utility.concat("Java", "Python")
utility.sum(10, 20)
utility.calculate(10, 30, "*")

print('--------------- alies from modul name------------------------------------------')

import utility as u

u.sum(10, 20)
u.concat("A", 1, 2)
u.calculate(20, 30, "/")

print('---------------alies from a function------------------------------------------')

from utility import sum as s  # (sum) shortcut (s)

print(s(10, 20))
