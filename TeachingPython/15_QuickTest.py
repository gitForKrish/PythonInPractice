userInput = int(input('Enter a number:'))
for i in range(1, userInput + 1): #1,2,3,...,10
    print('*' * i)

c = userInput - 1 
while c > 0:
    print('*' * c)
    c -= 1    