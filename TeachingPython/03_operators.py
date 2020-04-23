# Python Operators
# Arithmatic Operators
a,b = 28,3
print("Add=",a+b)
print('Sub=',a-b)
print("Mul=",a*b)
print("Div=",a/b)
print("Mod=",a%b)
print("Floor=",a//b)
print("Exp=",a**b)

# Assignment Operators
a=b
print(a)
a+=b # a = a+b
print(a)

a-=b #a = a-b
print(a)
a*=b
print(a)
a,b = 28,3
a%=b
print(a)

a,b = 28,3
a//=b
print(a)
a,b = 28,3
a**=b
print(a)

# Logical Operators
a,b = True,False
print(a and b)
print(a or b)
print(not a)
print(True and False)

# Bitwise operators
a,b = 5,3 # 1010 0011
print(a & b)
print(a | b)
print(a ^ b)
print(~a)

# Identity Operator
today = "thuesday"
weekend = "friday"
print(today is weekend)
print(today is not weekend)

# membership operator
#  in, not in
stud = ["ram", 'shyam', 'jack', 'jadhu']
print('madhu' in stud)
print('madhu' not in stud)