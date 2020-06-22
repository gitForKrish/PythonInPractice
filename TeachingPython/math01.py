'''
    1.Find the greatest and the smallest numbers:
    (i) 71834, 75284, 571, 2333, 594
    (ii) 9853, 7691, 9999, 12002
'''
list1 = (71834, 75284, 571, 2333, 594)
list2 = (9853, 7691, 9999, 12002)


def find_max_min(numbers):
    max = min = numbers[0]
    for i in range(1, len(numbers)):
        if max < numbers[i]:
            max = numbers[i]
        if min > numbers[i]:
            min = numbers[i]
    return max, min


result1 = find_max_min(list1)
result2 = find_max_min(list2)

print(f"First List: Max = {result1[0]}, Min = {result1[1]}")
print(f"Second List: Max = {result2[0]}, Min = {result2[1]}")
