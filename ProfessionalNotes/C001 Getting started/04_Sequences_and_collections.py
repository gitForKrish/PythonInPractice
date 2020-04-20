# tuple: An ordered collection of n values of any type. 
# - supports indexing 
# - hashable if all its members are hashable
# - immutable
myTuple = (1, 'c', 'python', (10,20), True)
print(myTuple)

# list: An ordered collection of n values. 
# - supports indexing 
# - not hashable
# - mutable
myList = [1, 'List Item', (1,2), ['hello', 'list'], False]
print(myList)

# set: An unordered collection of unique values. 
# - doesn't support indexing because of unordered behaviour
# - must be hashable
# - mutable
mySet = {1,'a',2}
print(mySet)

# dict: An unordered collection of unique key-value pairs; 
# - support custom indexing 
# - keys must be hashable
# - mutable
myDict1 = {1:'one', 2:'two'}
myDict2 = {'a':[1,2,3], 'b':'a string'}
print(myDict1, myDict2)