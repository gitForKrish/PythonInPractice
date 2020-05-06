# 2. Design a Grade System based on student marks.
# 	○ Collect marks from user.
# 	○ Print Grade based on the below hierarchy
# 		§ 90 & above: Grade A
# 		§ 70 & above: Grade B
# 		§ 60 & above: Grade C
# 		§ Less than 60: Grade D
# mark = input('Enter your marks:')
# while(mark !='e' and mark !='E'): 
#     mark = int(mark)   
#     if (mark >= 0 and mark <= 100):
#         if mark >= 90:
#             print("Grade A")
#         elif mark >= 70:
#             print("Grade B")
#         elif mark >= 60:
#             print("Grade C")
#         else:
#             print("Grade D")
#         break
#     else:
#         print('Invalid input. Valid Mark range: 0-100')
#         print("Please retry with valid mark!--OR-- Press E for exit")
#         mark = input()

# 4. Design a Login System based on the followings -
#     - Collect User Name and Password from Users
#     - Match the credential against user name - "admin" and password - "admin123"
#     - On successful match, Print - "Valid User" message
#     - On failure, Print - "Invalid User" message

# name = "\n\t    pur\tnendu mandal    \t\n" # Whitespace
# print(name)
# # Stripping
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())


# username = input('Enter User Name: ') 
# username = username.strip()
# password = input('Enter password for Login: ')
# if (username == 'admin' and password == 'admin123'):
#     print('Valid User')
# else:
#     print('Invalid User')

# 5. Create a list of your favourite food items, the list should have minimum 5 elements.
#     - List out the 3rd element in the list.
#     - Add additional item to the current list and display the list.
#     - Insert an element named Strawberry at the 3rd index position of the list and print out the list elements.

# fav_foods = ['apple', 'orange', 'banana', 'grape', 'cocunut']
# print(fav_foods[2])
# fav_foods.append('papaya')
# print(fav_foods) 
# fav_foods.insert(2,'strawberry')  #fav_foods[2] = 'strawberry'
# print(fav_foods)

# print(fav_foods[len(fav_foods)-1])
# print(fav_foods[-1])
# print(fav_foods[-len(fav_foods)])

# del fav_foods[-1]
# print(fav_foods)

# deletedItem = fav_foods.pop()
# print(deletedItem)
# print(fav_foods)

# deletedItem = fav_foods.pop(2)
# print(deletedItem)
# print(fav_foods)

# fav_foods.remove('banana')
# print(fav_foods)

# 6. Using a for-loop and a range function, print "I am a programmer" 5 times.
# for i in range(5):
#     print(i+1,".\t","I am a programmer")

# for i in range(5):
#     print(f"{i+1}.\tI am a programmer")

# name = 'purnendu'
# print(f"Hello {name}")

# 7. Create a function which displays out the square values of numbers from 2 to 9
for i in range(2,10): # [2, 3, 4, 5, 6, 7, 8, 9]
    i = i ** 2
    print(i)

i = 2
while i < 10:
    x = i ** 2
    print(x)
    i += 1
print(list(range(2,10)))

# List Comprehension
squares = [i**i for i in range(1,10)]
print(squares)

# 8. Write Python code which accepts name of a product and in turn returns their respective prices. 
#     - Make sure to use dictionaries to store products and their respective prices.
#     - The dictionary should include at least 5 elements.
# Soap - 25
# HandSanitizer - 50
# Shampoo - 100
# Surf - 75
# VimBar - 20
productDictionary = {
    "Soap":25,
    "HandSanitizer":50,
    "Shampoo":100,
    "Surf":75,
    "VimBar":20,
}
print(productDictionary)

# 9. List out  all the odd numbers from 1 to 100 using lists in Python.
oddNumbers = [i for i in range(1,100,2)]
print(oddNumbers)

oddNumbers = []
for i in range(1,100,2):
    oddNumbers.append(i)
    #print(oddNumbers) #[1], [1,3], [1,3,5] ... [99]
print(oddNumbers)
