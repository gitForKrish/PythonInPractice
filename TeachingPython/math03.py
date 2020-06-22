'''
5. Write all possible 2-digits numbers that can be formed by using the digits 2, 3 and 4. 
Repetition of digits is not allowed. Also find their sum.
output: 23,24,32,34,42,43 - > 
'''


def find_numbers(digits, decimal_place):
    generated_numbers = []
    for (index, value) in enumerate(digits):  # 2,3,4
        remaining = digits[:]                 # 0,1,2
        remaining.pop(index)

        for (ind2, val2) in enumerate(remaining):
            generated_numbers.append(value * 10 + val2)
    return generated_numbers


numbers = find_numbers([2, 3, 4, 5, 6], 2)
print(numbers)
print(len(numbers))
