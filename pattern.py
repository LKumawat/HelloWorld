for i in range(0, 5):
    for j in range(0, 5):
        print("*", end="")
    print()

print("printing F pattern...")
ls = [5, 2, 5, 2, 2]
# one way
for i in ls:
    print('X' * i)

# another way
print("printing F pattern with diff way...")

for i in ls:
    output = ''
    for j in range(i):
        output = output + 'X'
    print(output)

print("printing L pattern.")
l_list = [2, 2, 2, 2, 7]
for i in l_list:
    output = ''
    for j in range(i):
        output = output + 'X'
    print(output)

print("printing Left * pattern.")
for i in range(0, 5):
    op = ''
    for j in range(i):
        op += '*'
    print(op)

# or
print("printing Left * pattern in diff way")
for i in range(6):
    print('*' * i )
