'''
- No need to declare a variable in advance 
- No need to assign a data type to a variable
- Assigning a value to a variable itself declares and initializes the variable with that value
- No way to declare a variable without assigning it an initial value
- Variable names are case sensitive
'''
# Dynamic Type System
myVar=912345
print(myVar,type(myVar))  # 912345 <class 'int'>

myVar = 31.453
print(myVar,type(myVar))  # 31.453 <class 'float'>

myVar="My String"
print(myVar,type(myVar))  # My String <class 'str'>

myVar ='S'
print(myVar,type(myVar))  # S <class 'str'>

myVar = True
print(myVar,type(myVar))  # True <class 'bool'>

myVar = None
print(myVar,type(myVar))  # None <class 'NoneType'>

# assign multiple values to multiple variables
a,b,c = 1,2,3
print(a,b,c)

a,_,c = 1,2,3 # _ is a placeholder
print(a,c)

# a, b, c = 1, 2  # ValueError: need more than 2 values to unpack
# a,b = 1,2,3     # ValueError: too many values to unpack

x=y=[7,8,12] # assigning list object
print(x,y)
x=[1,2,3] # x is now pointing to different object
print(x,y)

m=n=[5,10,15]
print(m,n)
m[0]=20 # altering the object itself
print(m,n)

# nested list
x = [1,[2,3,4],5]
print(x[1])
print(x[1][2])


# Block Indentation
def myFunction():
  a=2
  return a
print(myFunction())

a,b=1,2
if a>b:
  print(a)
else:
  print(b)

# OR
if a<b: print(a)
else: print(b)

def Will_be_implemented_later():
  pass  # command that do nothing