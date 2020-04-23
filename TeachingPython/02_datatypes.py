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
 <menu>
    <breakfast>
        <name>Idli Vada</name>
        <price>25</price>
        <description>popular, sort-of-staple food in the South Indian states</description>
        <calories>150</calories>
    </breakfast>
    <lunch>
        <name>Idli Vada</name>
        <price>25</price>
        <description>popular, sort-of-staple food in the South Indian states</description>
        <calories>150</calories>
    </lunch>
    <dinner>
        <name>Idli Vada</name>
        <price>25</price>
        <description>popular, sort-of-staple food in the South Indian states</description>
        <calories>150</calories>
    </dinner>
</menu>

 3 - Unpack tuple values: julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
 
 4 - Access the value 3 from this collection -> [1,[2,3,4],5]

 5 - Which collection is suitable for the below requirements
    User wants to store the following subject in a variable - mathematics, python, data sturcture, big data
    In future, user also wants to modify the list according to his/her choice.
'''

myWorkingDays = ("monday", "tuesday", "wednesday", "thursday", "friday")
thirdWorkingDay = myWorkingDays[2]
print(thirdWorkingDay)

myTodaysMenu = {
    "menu":{
        "breakfast":{"name":"Idli Vada","price": 25, "description":"popular, sort-of-staple food in the South Indian states", "calories":150},
        "lunch":{"name":"Idli Vada","price": 25, "description":"popular, sort-of-staple food in the South Indian states", "calories":150},
        "dinner":{"name":"Idli Vada","price": 25, "description":"popular, sort-of-staple food in the South Indian states", "calories":150}
    }
}

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

(name, title, dob,_,releaseyear, profession, city) = julia
print(name)

myList = [1,[2,3,4],5]
print(myList[1][1])

myData = ["mathematics", "python", "data sturcture", "big data"]
myData[2] = "Data science"
print(myData)

st = "hello"
inputValue = 5
print(st+str(inputValue)) # Type Conversion
isValid = True
print(str(isValid))

print(True)
# print(type(True==1))

# issubclass()
# isinstance()
print(issubclass(bool, int))
print(True==1)

print(isinstance(True, bool))
print(isinstance(4.5, int))
print(isinstance(1, bool))
print(isinstance(1, int))


print(isinstance("\n", str))
print(isinstance("5", int))
print(isinstance(4.5e10, float))
print(issubclass(int, float))