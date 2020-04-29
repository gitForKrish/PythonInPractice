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

try:
    a,b = 20,0
    print(a/b)
except ZeroDivisionError:
    print('Division by zero occurred')
finally:
    print('Execute no matter what')