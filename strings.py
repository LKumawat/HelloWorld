# single, double, triple quotes
course1 = "Python's for beginners."
course2 = 'It is for "Beginners"'
print (course1)
print (course2)
course3 = ''' 
Hi Dev, 

Here is my first mail from university.

Thanks,
Lalita
'''
print(course3)
# accessing string's indices. start with 0 and reverse starts with -1;
# this range excludes the last number defined in range; [:] - It's used to print/copy same string
print(course1[0])
print(course2[-2])
print(course1[0:4])
print(course1[:7])
print(course1[2:])
print(course1[:])

another = course2[:]
print(another)
name = 'Jennifer'
print(name[1:-1])

# formatted string
first = 'Lalita'
last = 'Kumawat'
print(first + ' [' + last + '] is coder. ')
print(f'{first} [{last}] is coder. ')

# count the number of char
course1_len = len(course1)
print(f'length is string "{course1}" is: {course1_len}.')

# string methods ; create new updated string; case sensitive
print(course1.upper())
print(course1.find('o'))
print(course1.find('beginners'))
print(course1.find('Beginners'))
print(course1.replace('beginners', 'absolute beginners'))

# difference between in and find -> 'in' returns boolean and 'find' returns index
print('It' in course2)
print('python' in course1)

