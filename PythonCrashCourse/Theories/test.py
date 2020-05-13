# [3,4,5,3,7,2,8,3,2,5]
# user input - n

def find_freq_v1(n, numList):
    counter = 0
    for item in numList:
        if n == item:
            counter += 1
    return counter

def find_freq_v2(n, numList):
    counter = 0
    for i in range(len(numList)):
        if n == numList[i]:
            counter += 1
    return counter

def find_freq_v3(n, numList):
    counter = 0
    c = 0
    while(c < len(numList)):
        if n == numList[c]:
            counter += 1
        c += 1
    return counter

numbers = [3,4,5,3,7,2,8,3,2,5]
num = int(input('Enter a number to find frequency: '))
result = find_freq_v1(num, numbers)
print(f"Number: {num} -> Frequency: {result}")
result = find_freq_v2(num, numbers)
print(f"Number: {num} -> Frequency: {result}")
result = find_freq_v3(num, numbers)
print(f"Number: {num} -> Frequency: {result}")

numbers = [3,4,5,3,7,2,8,3,2,5,1,2,3,4,5]
num = int(input('Enter a number to find frequency: '))
result = find_freq_v1(num, numbers)
print(f"Number: {num} -> Frequency: {result}")
result = find_freq_v2(num, numbers)
print(f"Number: {num} -> Frequency: {result}")
result = find_freq_v3(num, numbers)
print(f"Number: {num} -> Frequency: {result}")