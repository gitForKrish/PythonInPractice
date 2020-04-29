# ------------------------Dictionary----------------------------
people = {"John": 32, "Rob": 23}
print(people["John"])
print(people["Rob"])
# Key can be of arbitary data type and value will be associated with it

numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(numbers[2])

# Check for Key existance
print(2 in numbers)
print(5 in numbers)

# Fetching the value from dictionary with default
print(numbers.get(2))
print(numbers.get(5))
print(numbers.get(5, "Key not found"))

# List Slicing
numbers = [0,100,200,300,400,500,600]
print(numbers)
print(numbers[1:4])     # end index is exclusive
print(numbers[:4])      # consider left side 0-3
print(numbers[3:])      # consider right side 3-end
print(numbers[1:6:2])    # 2 is the step, default step is 1
print(numbers[1:5:3])    # 2 is the step

# List Comprehension - keeping a rule for each item
nums = [x**2 for x in range(10)]
print(nums)

nums = [x**2 for x in range(10) if x**2 % 2 == 0]
print(nums)

# string formatting
number = [4,5,6]
newStr = "Numbers: {0}{1}{2}".format(number[0], number[1], number[2])
print(newStr)
newStr = "Numbers: {0},{1},{2}".format(number[0], number[1], number[2])
print(newStr)

date = [12,12,2020]
formattedDate = "Date: {0}/{1}/{2}".format(date[0], date[1], date[2])
print(formattedDate)

msg = "{x} times {y}".format(x = 5, y = 2)
print(msg)

# String Functions
# Join
print(",".join(['4','5','6']))
print(":".join(['4','5','6']))

#Replace
print("Hello there".replace("there", "world"))

# Start and End of String
myStr = "This is a string"
print(myStr.startswith("This"))
print(myStr.startswith("this"))

print(myStr.endswith('string'))
print(myStr.endswith('String'))

#Uppercase & Lowercase
print("Hello, how are you?".upper())
print("Hello, how are you?".lower())

# Numeric function
# min fn
print(min(4,8,2,6,7,9))
print(max(4,8,2,6,7,9))
print(abs(-203))
