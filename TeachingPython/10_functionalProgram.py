# Function as argument
def addTen(x):
    return x + 10

def twice(func, arg):
    return func(func(arg))

print(twice(addTen, 15))

# lambda - annonymous function, no return statement (as always return the expression), one liner
result = lambda x: x**2
print(result(20))

# Map - works on iterable, apply a rule for each item
def add(x):
    return x  + 2

myList = [10,20,30,40]
myMap1 = map(add, myList)
print(list(myMap1))

myMap2 = map(lambda x: x*2, myList)
print(list(myMap2))


#filter - filtering iterable, apply a rule to filter each item
myList = [4,5,2,6,3,7,8,9,11,1]
myFilter = filter(lambda x: x%2==0, myList)
print(list(myFilter))

#generators - similar like list but doesn't have indexing
def show():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1
print(list(show()))

def showEven(x):
    for i in range(0, x + 1):
        if i%2==0:
            yield i
print(list(showEven(20)))
print(list(showEven(200)))