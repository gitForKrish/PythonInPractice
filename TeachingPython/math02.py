'''
    2. Interchange the values between given indexes:
    71834, 75284, 571, 2333, 594
    0       1       2   3     4
    Indexes(Zero-base index): 2,4 and 1,4
    71834, 75284, 594, 2333, 571 
    71834, 594, 571, 2333, 75284
'''


def interchange_values(numbers, index1, index2):
    mylist = list(numbers)
    temp = mylist[index1]
    mylist[index1] = mylist[index2]
    mylist[index2] = temp
    numbers = tuple(mylist)


mytuple = 71834, 75284, 571, 2333, 594
# print(interchange_values(mytuple, 2, 4))
# print(interchange_values(mytuple, 1, 4))
interchange_values(mytuple, 2, 4)
print(mytuple)
