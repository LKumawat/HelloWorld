# for loop
for item in 'Python':
    print(item)

print("printing a list")
# List
for item in [1,2,3,4,5,6]:
    print(item)


print("printing a list with range")
# range(start, end, step)
for item in range(8):
    print(item)

for item in range(1,9,2):
    print(item)

prices = [10, 20, 50, 80, 110]
total = 0
for items in prices:
    total = total + items
print(f'Total price of items in cart is: {total}')

for x in range(4):
    for y in range(4):
        print(f'({x},{y})')