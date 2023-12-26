
for i in range(1, 6):
    print(i)
    if i == 3:
        break  # we are breaking the loop at 3

print('-------skip-condition--------------')

for i in range(1, 6):
    if i == 3 or i == 4:
        continue
    print(i)

print('-------pass-condition--------------')

for i in range(1, 6):
    if i == 3 or i == 4:
        pass  # the main purpose of PASS is to work on the body latter on
        # also is used to achievement Abstraction (hiding the implementation)
    print(i)