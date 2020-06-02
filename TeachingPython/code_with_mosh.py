from timeit import timeit
multiline_string = """
this
is
a
multiline
string
"""
print(multiline_string)

# Falsy Values
print(bool(False))
print(bool(""))
print(bool(0))
print(bool(None))
print(bool([]))
print(bool({}))

# numeric representation of character
print(ord('A'))  # 65
print(ord('~'))  # 126
print(ord('╚'))  # 9562

# Ternary Operator
age = 15
eligible_for_voting = "yes" if age >= 18 else "no"
print(eligible_for_voting)

# Not logical operator
is_raining = False
if not is_raining:
    print('Not raining...')

# Chaining
age = 17
if 1 <= age <= 18:
    print('You are not eligible for voting')
else:
    print('You are eligible for voting')

# For-Else Block
successful = False
for i in range(1, 6):
    print('Attempting'+'.' * i)
    if successful:
        print('Login successful')
        break
else:
    print(f"Tried {i} times and failed")

# Function with varying arguments


def multiply(*numbers):
    print(numbers)
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 5, 6, 3, 7, 9))
print(multiply(2, 7, 5, 9, 4, 6, 1, 5))

# Function with varying Key-Value arguments


def save_user(**user):
    print(user)
    print(f"User - {user['name'].title()} is saved")


save_user(id=1, name='krish', age=31)
save_user(id=2, name='purd', age=30)

# List
# List with initial values
ten_zeros = [0]*10
print(ten_zeros)

five_users = ['default name'] * 5
print(five_users)

numbers = [4, 7, 1, 5, 2, 8]
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])

# Exceptions are costly operation

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age can not be less than equals to 0")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

value = calculate_xfactor(-1)
if value == None:
    pass
    # print("age can not be less than equals to 0")
"""
print(timeit(code1, number=10000))
print(timeit(code2, number=10000))
