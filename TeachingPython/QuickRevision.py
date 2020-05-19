'''
Hello World Program Using Python
'''
print('Hello World')
'''
Identifiers
Variables
'''
x = 10
print(x)
x = 'hello'
print(x)
'''
Data Types
Immutable Data Types
Numeric Data Type
Strings
Tuples
Mutable Data Type
Lists
Dictionaries
Sets
'''
x = 50
type_of_x = type(x)
print(type_of_x)
print(type(x))

# Collection of values - Tuple
numbers = (5,7,9,18,15,"Purnendu",True)
print(numbers[0])
print(numbers[5])
print(len(numbers))
print("-----------------------------------")
for element in numbers:
    print(element)
print("-----------------------------------")
for index in range(len(numbers)):
    print(numbers[index])

mylist = [50, False, 'hello', (10,15), ['sunday','monday','friday']]
print(mylist[1])
print(mylist[3][1])
mylist[4][1] = 'wednesday'
print(mylist[4][1])
# mylist[3][1] = 20
# print(mylist[3][1])

mydict = {'age':28,'name':'purd',  10:'medal'}
print(mydict)
print(mydict.keys())
print(mydict.values())

myset = {4,5,7,8,5,4}
print(myset)
'''
Python Operators
Arithmetic Operator
Assignment Operator
Comparison Operator
Logical Operators
Bitwise Operator
Identity Operator
membership Operator
'''
print(10+20)
x = 10
print(x)
print(x == 10)
print(x != 10)
print(x > 10)
print(x >= 10)
print(x < 10)
print(x <= 10)

x = 10;y=20
# x equal 10 and y equal 20
print(x==10 and y == 20)
print(x==10 and y != 20)
print(x==10 or y != 20)
# x except the value 10 

nonwokringDays = ['sunday','saturday']
myday = 'sunday'
print(myday in nonwokringDays)
myday = 'monday'
print(myday in nonwokringDays)
myday = 'sunday'

print(myday is nonwokringDays[0])
'''
Conditional Statements
'''
a,b = 20,10
if(a>b):
    print(a)
else:
    print(b)
'''
Loops on Python
While Loop
For Loop
Nested Loops
'''
i = 0
while (i < 11):
    print(i)
    i+=1

for i in range(11):
    print(i)

# print all number except 5
print("-------------------------------------")
c=0
while c < 11:
    if c == 5:
        c += 1
        continue
    else:
        print(c)
    c += 1
print("-------------------------------------")
# takes name as user input  but if user q for quit
while True:
    name = input('name: ')
    if name == 'q':
        break
    print(f"Hello {name}")

print("-------------------------------------")
'''
Control Statements
Functions
'''
# given two user input, find the first common divider except 1
# def first_common_divider(num1, num2):
# 12 - 2,3,4,6,12
# 18 - 2,3,6,9,18
# Output: 2

def find_divisor_without_1(x):
    list_of_x = []
    for i in range(2, x + 1):
        if x % i == 0:
            list_of_x.append(i)
    return list_of_x

x = 7
print(find_divisor_without_1(x))

x = 24
print(find_divisor_without_1(x))

x = 7
y = 14
list_of_x = find_divisor_without_1(x)
list_of_y = find_divisor_without_1(y)

print(list_of_x)
print(list_of_y)

for element_in_x in list_of_x:
    if element_in_x in list_of_y:
        print(f'first_common_divider = {element_in_x}')
        break
