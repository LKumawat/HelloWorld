print("Lalita Kumawat")
print("0 -------")
print(" !!!!")
print("@" * 10)

# defining variables
name1 = "John Smith"
age= 20
is_newpatient = True


# asking for input
#activity = input('What are you doing ? ')
#print('Hey, ' + activity )

name = input('Whats your name ?')
color = input('What is your favourite color ?')
print(name + ' likes ' + color + '.')


# input function always give string. int(). float(), bool() are used to convert a string into int, float and bool
weight_pound = input('What is your weight in pound ? \n' )
type(weight_pound)
weight_kg = 0.453592 * float(weight_pound)
type(weight_kg)
# print(weight_kg)
print('Your weight in kg is ' + str(weight_kg))

