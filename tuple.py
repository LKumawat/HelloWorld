# immutable, can't modify like lists, written in () istead of [] like list
tup = (1,2,3,5,8)
print(tup.count(2))

# unpacking
coordinates = (2, 5, 9)

# either we can define like below  or
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# this method also can be used for list
x, y, z = coordinates
print(x)
print(y)

