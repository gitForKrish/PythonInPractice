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
