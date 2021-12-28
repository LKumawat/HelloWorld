ls = [2, 65, 21, 2, 119, 3]

max = ls[0]
for num in ls:
    if num > max:
        max = num
print(max)

ls.append(25)
print(ls)

ls.insert(2, 105)
print(ls)

print(ls.index(65))

ls.remove(21)
print(ls)

# ls.clear()
# remove last item in list
ls.pop()
print(ls)

print(ls.index(65))
print(ls.count(2))

ls.sort()
print(ls)

ls.reverse()
print(ls)

ls2 = ls.copy()
print(ls2)


# remove duplicates
list1 = [2, 5, 21, 2, 19, 5]
uniques = []
for number in list1:
    if number not in uniques:
        uniques.append(number)
print(uniques)


