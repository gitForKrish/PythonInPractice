'''
3. Calculate the Factorial of an user provided number. (Try with For and While loop)
'''
# 5: 
for i in range(11):
    print(i)

c = 0
while c <= 10:
    print(c)
    c += 1

myNumber = [2,3,7,4,11,8,9,7]
c = 0
while(c < len(myNumber)):
    if myNumber[c] == 7:
        c += 1
        continue
    print(myNumber[c], end=" ")
    c += 1            
print(myNumber)