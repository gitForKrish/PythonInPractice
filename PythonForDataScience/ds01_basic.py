# Python Keywords
import keyword

keywords = keyword.kwlist
print(f"Total python keywords = {len(keywords)}")
print(f"Here are the keyword list:\n{keywords}")

print("*"*100)
# Loops: While-else and For-else
nums = [10, 12, 15]
index = sum = 0
while(index < len(nums)):
    sum += nums[index]
    # if nums[index] == 12:
    #     break
    index += 1
else:
    print('No more items left')
print(f"Sum total = {sum}")

sum = 0
for num in nums:
    sum += num
    # if num == 12:
    #     break
else:
    print('No more items left')
print(f"Sum total = {sum}")
print("*"*100)

# Multiline Statements / Assignment
a = 1 + 2 + 3 + \
    4 + 5 + \
    6
print(a)

a = (1 + 2 + 3 + 
    4 + 5 + 
    6)
print(a)

a = 10; b = 15; c = 20
print(a,b,c)

a,b,c = 10,15,20
print(a,b,c)

a=b=c=10
print(a,b,c)
print("*"*100)

# Storage Location
x = 3
print(id(x))

y = 3
print(id(y))    # address is same as x

y = 2
print(id(y))

def add(x):
    return x + 10
print(id(add))
print("*"*100)

# Output Formatting
print("A is = {} and B is = {}".format(10,15))
print("A is = {1} and B is = {0}".format(10,15))
print("Hello {name}. Wish you a very {msg}".format(msg = "good morning", name = "Riyam"))