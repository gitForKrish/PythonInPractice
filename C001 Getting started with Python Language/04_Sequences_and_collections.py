# tuple: An ordered collection of n values of any type. Supports indexing; immutable; hashable if all its members are hashable
myTuple = (1, 'c', 'python', (10,20), True)
print(myTuple)

# list: An ordered collection of n values. Not hashable; mutable.
myList = [1, 'List Item', (1,2), ['hello', 'list'], False]
print(myList)

# set: An unordered collection of unique values. Items must be hashable.
mySet = {1,'a',2}
print(mySet)

# dict: An unordered collection of unique key-value pairs; keys must be hashable.
myDict1 = {1:'one', 2:'two'}
myDict2 = {'a':[1,2,3], 'b':'a string'}
print(myDict1, myDict2)
