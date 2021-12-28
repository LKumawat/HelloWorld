# search for "python 3 module index" in browser
import random


class Dice:
    def roll(self):
        random_tup = random.sample([1, 2, 3, 4, 5, 6], k=2)
        print(f'random dice list is... {random_tup}')

    def roll2(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice1 = Dice()
dice1.roll()

print("Second way for printing tuple in a dice ")
print(dice1.roll2())