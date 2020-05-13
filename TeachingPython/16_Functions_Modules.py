'''
Input Parameter: 45/-, Message, __
Function: Robot
Return Parameter: 1 Kg Sugar,__, __
'''

# Function - Named block of code
def greetings():
    print('Good Morning')

# greetings()
# greetings()

msg = greetings
msg()
print(type(msg))

def sayhello(name):
    return f"Hello {name.title()}. How are you?"

msg = sayhello('purnendu')
print(msg)
sayhello('krishnendu')
print(msg)

'''
8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
'''
def display_message():
    print('We have learnt Function...') 

display_message()

'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
'''
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Ramayana")
favorite_book("Mahabarata")