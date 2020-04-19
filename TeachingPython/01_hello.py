# Apr 16 - Comments, Variable, Identifier

# print("Hello Python")
# print("Hello Purnendu")

'''
x="purnendu"
print(x)
'''
'''
x=10
print("purnendu")
print(x)

x="krishnendu"
print(x)
'''

# Apr 17 - Hands on
# (10+5)*4 - using 3 variables, 2 variables, 1 variable
# 3 Variables -> (10+5)*4
# a = 10
# b = 5
# c = 4
a,b,c = 10,5,4
print((a+b)*c)

# 2 Variables -> (10+5)*4
p = 10
q = 5
p = p + q
p = p * 4
print(p)

# 1 Variables -> (10+5)*4
x = 10
x = x + 5
x = x * 4
print(x)

# Swap two number (with and without additional variable)
m = 10
n = 0
print(m,n) # 10, 5
# x = m
# m = n
# n = x
m = m + n
n = m - n
m = m - n
'''
10 = m      # Static Error
m = m * n
n = m // n  # Runtime Error - Exception Handling
m = m // n
'''
print(m,n) # 5, 10

# Unpack value with dummy placeholder
f,_,g = 10,5,4

b = 10
print(b, 4)