# A list is a collection of items in a particular order
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])                          # 2nd item
print(bicycles[3])                          # 4th item

print(bicycles[len(bicycles)-1])            # accessing last element
print(bicycles[-1])                         # accessing last element with negative index
print(bicycles[-len(bicycles)])             # accessing first element with negative index

#---------------------------Changing, Adding, and Removing Elements------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')                 # append the item to the list
# motorcycles[len(motorcycles)] = 'hero'    # IndexError: list assignment index out of range
print(motorcycles)

motorcycles.insert(0, 'hero')               # inserting elements into list

del motorcycles[0]
print(motorcycles)                          # removing an Item Using the del Statement

last_item = motorcycles.pop()               # remove the last item from the list and return the deleted item
print(motorcycles)
print(last_item)

first_item = motorcycles.pop(0)             # remove the first item by pop() with index
print(motorcycles)
print(first_item)

# when you want to delete an item from a list and not use that item in any way, use the del statement; 
# if you want to use an item as you remove it, use the pop() method

motorcycles.remove('yamaha')                # Removing an Item by Value
print(motorcycles)

#---------------------------Organizing a List------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                                 # Sorting a List permanantly - ascending order (default)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)                     # sorting the list in descending order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))                         # Sorting a List temporarily
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()                              # Printing a List in Reverse Order
print(cars)

print(len(cars))                            # find the length of the list