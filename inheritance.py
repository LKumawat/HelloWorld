class Mammal:
    def walk(self):
        print("Walk...")

class Dog(Mammal):
#    pass
# we can simply write pass if that class is empty, which means None
    def bark(self):
        print("bark..")

class Cat(Mammal):
    def annoying(self):
        print("Annoying...")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.annoying()

