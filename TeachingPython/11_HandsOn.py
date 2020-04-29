# 1. Take 3 numeric values as input from User. Find out Max & Min.
#  21 35 11

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
max = min = 0
if a >= b and a >= c:
    max = a 
    if b >= c:
        min = c
    else:
        min = b  
elif b >= a and b >= c:
    max = b
    if a >= c:
        min = c
    else:
        min = a
else:
    max = c
    if a >= b:
        min = b
    else:
        min = a

print("Max: " + str(max))
print("Min: " + str(min))


import myMath
numbers = [10,29,34,21,8,6,4, -1000, 1000, float("-inf")]
print("Max:", myMath.max(numbers))
print("Min:", myMath.min(numbers))