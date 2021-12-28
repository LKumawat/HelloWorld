# class-> first letter is always capital in class name.
# defines methods and objects with attributes.
# Each object is different instance of class. These object's attributes can be defined anywhere in the program.

class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)


# Defining constructor
# self is reference of current obj; thie below __init__ method is used to construct the object.

class pnt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

pnt1 = pnt(2,6)
pnt2 = pnt(8,4)
#pnt1.x = 2
print(pnt1.y)
print(pnt2.x)


# exercise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking...')

lk = Person("Lalita Kumawat")
print(lk.name)
lk.talk()
dev = Person("Devender Kumawat")
dev.talk()