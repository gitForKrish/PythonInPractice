def min(numbers):
    mini = float('inf')
    for i in range(len(numbers)):
        if numbers[i] < mini: 
            mini = numbers[i]
    return mini

def max(numbers):
    maxi = float('-inf')
    for i in range(len(numbers)):
        if numbers[i] > maxi: 
            maxi = numbers[i]
    return maxi