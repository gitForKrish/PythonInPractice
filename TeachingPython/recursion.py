# 5! = 5*4*3*2*1 = 120
def fact(num):
    if num == 0:
        return 1
    elif num < 0:
        return None
    f = 1
    for i in range(1, num + 1): # 1,2,3,4,5
        f = f * i
    return f

num = int(input('enter a number:'))
print(fact(num))

# fact(5) = 5 * fact(4)
#                4 * fact(3) ... fact(0) = 1
# fact(n) = n * fact(n-1)

def fact_rec(n):
    if n == 0:
        return 1
    elif n < 0:
        return None
    return n * fact_rec(n-1)

print(fact_rec(num))