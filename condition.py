good_credit = False
print("The price of house is $1M.")
if good_credit:
    print("you have a good credit score so you need to put down 10%.")
    down_payment1 = 10
else:
    print("You don't have a good credit score so you need to put down 20%.")
    down_payment1 = 20

down_payment = 1000000 * down_payment1 / 100
print(f'Down payment is: ${down_payment}')

# high income or good credit, no criminal record then eligible for loan

has_high_income = False
has_good_credit = False
has_criminal_record = False

if has_high_income or has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# compare condition
temp = 20
if temp > 30:
    print("Its a hot day!")
elif temp < 10:
    print("Its a cold dat!")
else:
    print("Its neither cold nor hot!")

#
name = "ldkslfjorihgervf wg"
# name = input("Please enter the name")
if len(name) < 3:
    print("Name must have at least 3 characters.")
elif len(name) > 50:
    print("Name must have less than 50 characters.")
else:
    print("Name looks good!")

# exercise
weight = input("Weight: ")
# weight = float(input("Weight: "))

unit = input("(L)bs or (K)g ")

# if unit == "lbs" or unit == "LBS" or unit == "Lbs":
if unit.upper() == "L":
    wt = float(weight) * 0.453592
    print(f'You are {wt} kgs. ')
else:
    wt = float(weight) / 0.453592
    print(f'You are {wt} pounds.')

