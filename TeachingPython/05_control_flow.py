# loop - for, while
# print 1 - 20

# i = 1
# print(i)

# i += 1
# print(i)

# i += 1
# print(i)

for i in range(20): # 1 para - stop(exclusive)
    print(i+1)

# for i in range(1,21): # 1 para - stop(exclusive)
#     print(i)

# for i in range(1,20): # 2 para - 1st: start value (inclusive), 2nd: stop value (exclusive)
#     print(i)

# for i in range(1, 20, 5): # 3 para - 1st: start value (inclusive), 2nd: stop value (exclusive), 3rd: step
#     print(i)

# for i in range(1, 20, 5, 4): # 3 para - 1st: start value (inclusive), 2nd: stop value (exclusive), 3rd: step
#     print(i)

# pass
# continue
# break

# Logical operator - or, and

# Hands on
# - print all number divisible by 5 upto 100
for x in range(101):
    if(x % 5 == 0):
        print(x)

for x in range(0,101,5):
    print(x)
# - print number of * based on the number value upto 10
'''
1 - *
2 - **
3 - ***
...
10 - **********
'''
for x in range(11):
    for y in range(x):
        print('*', end="")
    print()

# - User input for triangle formation - 2
userInput = input("Enter a numeric value for triangle formation:")
userInput = int(userInput)
for x in range(userInput + 1):
    print('*'*x)

# Print prime numbers upto 100
# - print all number divisible by 5 upto 100
# - print the below as per user input: 4
'''
*
**
***
****
***
**
*
'''

# print(10, end="Hello")
# print(20)