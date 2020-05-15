'''
10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far.
Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter.
Write a program that reads the file and prints what you wrote three times.
Print the contents once by reading in the entire file, once by looping over the file object,
and once by storing the lines in a list and then working with them outside the with block.
'''
file_name = 'p09_handsOn_Dummy.txt'

with open(file_name) as file_obj:
    contents = file_obj.read()

print(contents)
print('-------------------------------------------------------------------')

with open(file_name) as file_obj:
    for line in file_obj:
        print(line)
print('-------------------------------------------------------------------')

with open(file_name) as file_obj:
    lines = file_obj.readlines()

    for line in lines:
        print(line)
print('-------------------------------------------------------------------')

'''
10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
  message = "I really like dogs."
  message.replace('dog', 'cat') -> 'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C.
Print each modified line to the screen.
'''
with open(file_name) as file_obj:
    lines = file_obj.readlines()

    for line in lines:
        line = line.replace('Python', 'C#').strip()
        print(line)
print('-------------------------------------------------------------------')

'''
10-3. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
'''
name = input('Enter your name: ')

file_name = 'p09_guest.txt'
with open(file_name, 'w') as file_obj:
    file_obj.write(name)
print('-------------------------------------------------------------------')

'''
10-4. Guest Book: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.
'''
print('Info: Press "q" to quit anytime')
file_name = "p09_guest_book.txt"
with open(file_name, 'w') as file_object:
    while(True):
        name = input('enter your name: ')
        if name == 'q':
            break
        file_object.write(f"{name.title()} \n")
        print(f"{name.title()} is registered now")

print('-------------------------------------------------------------------')
'''
10-5. Programming Poll: Write a while loop that asks people why they like programming. 
Each time someone enters a reason, add their reason to a file that stores all the responses.
'''
file_name = 'p09_responses.txt'
print('Info: Press "q" to quit anytime')
while(True):
    response = input('Why you like programming? ')
    if response == 'q':
        break
    with open(file_name, 'a') as file_object:
        file_object.write(f"{response}\n")
