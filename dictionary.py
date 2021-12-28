# stores  key:values; represented with {}; can store string, number, list, boolean etc..; case sensitive
customers = {
    "name": "Lalita Kumawat",
    "age": 27,
    "is_graduated": True
}
print(customers["name"])
# Or we can use get function
print(customers.get("name"))
print(customers.get("birth_date", "10 may 1994"))
customers["birth_place"] = "Losal"
print(customers.get("birth_place"))

num_trans = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
#print("Enter number 1234")
phone = input("Phone: ")
#print(num_trans[1], num_trans[2], num_trans[3], num_trans[4])

# or for any random number
op = ""
for ch in phone:
    op += num_trans.get(ch, "!") + " "
print(op)

# emoji convertor
# Use control+command+space in mac for emojis
message = input("> ")
words = message.split(' ')
emojis = {
     ":)": "😀",
    ":(": "😟"
}
#print(words)
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

