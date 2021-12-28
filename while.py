# while loop
i = 1
while i < 5:
    print('*' * i)
    i += 1
print("Done")

# Guessing game...
'''
guess = input("Guess: ")
g = 1
if int(guess) == 9:
    print("You won!")
else:
    while g < 3:
        input("Guess: ")
        g += 1
    print("Sorry, you failed !")
'''

# another way
guess_count = 1
guess_limit = 4
while guess_count < guess_limit:
    guess2 = int(input("Guess: "))
    guess_count += 1
    if int(guess2 == 9):
        print("you won!")
        break
else:
    print("Sorry, you failed !")


matrix = [
    [2,5,3,6],
    [8,5,2,1]
]
print(matrix[1])
matrix[1][3] = 20
print(matrix[1][3])


for row in matrix:
    for item in row:
        print(item)



