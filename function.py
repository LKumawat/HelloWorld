# parameter are defined in function definition but arguments are passed in funcation call.
# keyword argument; increases readability; good for numerical values
# Always use keyword arguments after positional arguments if we are using both.
# By default all functions return None

def user_greet(name, act):
    print(f'Hi {name}!')
    print(f'How are you doing?')
    print(f'Do you wanna {act} ?')


print("Start...")
user_greet("Dev", "play")
# user_greet("Lalita", "dance")
# with keyword argument
user_greet("Lalita", act="dance")
print("Stop!")

# Creating a function for calculating square
def square(num):
    return (num*num)

number = input("Enter a number: ")
print(f' Square is:', square(int(number)))

# Creating a function for emoji converter


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😟"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))


