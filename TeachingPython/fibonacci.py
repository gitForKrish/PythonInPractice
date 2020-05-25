# 0 1 1 2 3 5 8 13 21 ...
# n = numbers to print

def fibo_while(num):
    x1,x2 = 0,1
    print(x1, x2, end = " ")

    counter = 3
    while counter <= num:
        xi = x1 + x2
        x1 = x2
        x2 = xi
        counter += 1
        print(xi, end=" ")

def fibo_for(num):
    a=0;b=1
    print(a,b,end=" ")

    for i in range(2, num): # 2,3,4
        c = a + b
        a = b
        b = c
        print(c, end=" ")

def fibo_recur(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    
    return fibo_recur(num-1) + fibo_recur(num-2)

n = int(input("enter a number to print Fibonacci series: "))
fibo_while(n)
print()
fibo_for(n)
print()
for i in range(1,n+1): # 1,2,3,4,..n
    print(fibo_recur(i), end=" ")