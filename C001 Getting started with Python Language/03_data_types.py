# data types
# 1. Boolean:  bool - True, False (T & F in Capital)
print(issubclass(bool, int))  # bool type is sub type of int type
print(isinstance(False, bool)) # True, False are the instances of bool type

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