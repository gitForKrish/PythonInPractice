# '''
# Built-in objects considered FALSE:
#  - constants defined to be false: None and False.
#  - zero of any numeric type: 0, 0.0, 0j
#  - empty sequences and collections: '', (), [], {}, set(), range(0)
# '''

# # print(type(range(10)))

# for i in range(10):
#     print(i)

# for i in range(5,20):
#     print(i)

# for i in range(5,20,5):
#     print(i)

# i = 10
# while(i > 0):
#     print(i)
#     i-=1

# i=5
# while(i>0):
#     for j in range(i):
#         print(i,end='')
#     print()
#     i-=1

# name=input("what is your name?")
# print(name)

# def add(x, y):
#     return x + y


# print(add(10,5))

# import random

# for x in range(5):
#     print(random.randint(1,6))


# def calculateBMI(w,m):
#     return w/(m**2)

# weight = float(input('enter your weight (in kg):'))
# height = float(input('enter your height (in meter):'))
# print(calculateBMI(weight, height))

# try:
#     a,b = 20,0
#     print(a/b)
# except ZeroDivisionError:
#     print('Division by zero occurred')
# finally:
#     print('Execute no matter what')

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

print(users)

for i,j in friendships:
    users[i]["friends"] = users[j]
    users[j]["friends"] = users[i]

print(users)