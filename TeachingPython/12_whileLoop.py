'''
3. Calculate the Factorial of an user provided number. (Try with For and While loop)
'''
# 5: 
# for i in range(11):
#     print(i)

# c = 0
# while c <= 10:
#     print(c)
#     c += 1

# myNumber = [2,3,7,4,11,8,9,7]
# c = 0
# while(c < len(myNumber)):
#     if myNumber[c] == 7:
#         c += 1
#         continue
#     print(myNumber[c], end=" ")
#     c += 1            
# print(myNumber)

# #5! = 5*4*3*2*1
# number = int(input("Enter a number for factorial:"))
# if number < 0:
#     print("Factorial can't be possible for negative number")
# else:
#     fact = 1
#     while (number >= 1):
#         fact = fact * number
#         number = number - 1
#     print(fact)

# Sum of first n natural number
num = int(input("Enter a number"))
if num < 0:
    print("Invald input")
else:
    sum = 0
    while (num >= 0):
        sum = sum + num
        num = num - 1
    print(sum)

# Calculate sum of 1st 20 odd number
sum = 0
num = int(input("Enter a number"))
for i in range(1, num*2+1,2):
    sum = sum + i
print(sum)