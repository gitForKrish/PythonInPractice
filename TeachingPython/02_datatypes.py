# Data Type - statically/dynamically typed language
# Immutable - numeric, string, tuple
# Mutuable - List, Dictionary, Set

# Numeric
# integer, float, complex number, boolean(true/false)
x = 10
print(type(x)) # <class 'int'>

x = 4.5
print(type(x)) # <class 'float'>

m = 4j + 3
n = -6 -5j
print(m+n)
print(type(m))

# Python is case-sensitive
myChoice = True,8,4.5,"Purnendu", 4+5j, 8
print(type(myChoice))
print(myChoice[3])
# myChoice[1] = 10

myList = [1,2,3,3]
print(type(myList))
print(myList[2])
myList[1] = 8
print(myList)

mySet = {1,2,3,3}
print(type(mySet))
mySet.add(5)
print(mySet)

myName = "Purnendu"
print(myName)
myName = 'Krishnendu'
print(myName)
print(type(myName))

myDictionary = {"name":"Purnendu", "age":30, "isMarried":True,"1":"Whar are you doing"}
print(type(myDictionary))
print(myDictionary["1"])

'''
Hands On 
 1 - Create a collection for the working days - monday, tuesday, wednesday, thursday, friday 
 
 2 - Create and access dictionary for the following -> 
    <breakfast>
        <name>Idli Vada</name>
        <price>25</price>
        <description>popular, sort-of-staple food in the South Indian states</description>
        <calories>150</calories>
    </breakfast>

 3 - Unpack tuple values: julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
 
 4 - Access the value 3 from this collection -> [1,[2,3,4],5]

 5 - Which collection is suitable for the below requirements
    User wants to store the following subject in a variable - mathematics, python, data sturcture, big data
    In future, user also wants to modify the list according to his/her choice.
'''