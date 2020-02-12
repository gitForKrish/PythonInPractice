a='123.45'
b=float(a)
# c=int(a) # ValueError: invalid literal for int() with base 10: '123.45'
d=int(b)

print(a,b,d)

print(int(float('123.45')))

a='hello'
print(tuple(a))
print(list(a))
print(set(a))