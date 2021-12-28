# When program crashes, it returns exic code 1 and successful code returns always 0.
try:
    age= int(input("Age: "))
    print(f'Age is  {age} .')
    income = 20000
    risk = income / age
    print(risk)

except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Age can't be zero")


