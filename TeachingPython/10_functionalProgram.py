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

'''
Assume you want to build two functions for discounting products on a website.
Function number 1 is for student discount which discounts the current price to 10%.
Function number 2 is for additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
Depending on the situation, we want to be able to apply both the discounts on the products.

Design the above two mentioned functions and apply them both simultaneously on the price.
'''
def applyDiscountForStudent(x):
    return x - x*0.1

def applyAddiDiscountForRegular(func, arg):
    studDisc = func(arg)
    return studDisc - studDisc*0.05

bookPrice = 240
print("Price for student:", applyDiscountForStudent(bookPrice))
print("Price for regular buyers:", applyAddiDiscountForRegular(applyDiscountForStudent, bookPrice))

# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.
myLambda = lambda x: x * (x + 5) **2
print(myLambda(5)) 

'''
Consider a list in Python which includes prices of all the items in a store.
Build a function to discount the price of all the products by 10%.
Use map to apply the function to all the elements of the list so that all the product prices are discounted.
'''
priceList = [100,200,300,400,500]
discountedPriceMap = map(lambda x: x-x*0.1, priceList)
print(list(discountedPriceMap))