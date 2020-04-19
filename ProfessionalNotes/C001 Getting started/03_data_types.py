# 1. Boolean:  bool - True, False (T & F in Capital)
# The bool type is a subclass of the int type and True & False are its only instances
print(issubclass(bool, int))    # bool type is sub type of int type
print(isinstance(False, bool))  # True, False are the instances of bool type

# If boolean values are used in arithmetic operations, their integer values will be used
print(True+True)
print(True*False==0)

# 2. Numbers: int, float, complex
a = 38563846326424324   # int in python is of arbitary size
b = 123456789.e1        # float depends on the system architecture 
c = 10+15j              # complex number

# 3. String: str(unicode string), bytes(byte string)
myStr = 'hello'
print(myStr)

myByteStr = b'hello bytes'
print(myByteStr)

myRawStr = r'raw \n string'
print(myRawStr)

# 4. tuple: An ordered collection
myTuple = (1,2.5,True,"hello tuple", (4,5))
print(myTuple)
print(type(myTuple))
print(myTuple[3])
# tuple is immutable
# myTuple[1] = 7.9 # TypeError

# 5. list: An ordered collection
myList = ['a', 1, (4,5), [10, 15]]
print(myList)
print(type(myList))
print(myList[2][1])
myList[3][0]=11
print(myList)

#6. set: An unordered collection of unique values
mySet = {1,2,3,3}   # redundant value will be removed at the time of initialization
print(mySet)
print(type(mySet))
# as set is unordered, you can't access element through index