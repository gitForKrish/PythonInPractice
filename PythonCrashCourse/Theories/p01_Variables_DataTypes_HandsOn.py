'''
2-1. Simple Message: Assign a message to a variable, and then print that message.
'''
message = "Welcome to the world of Python"
print(message)

'''
2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new message.
'''
message = "You will find so many things to explore"
print(message)

'''
2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
'''
person = "Jackson"
print(f"Hello {person}, how are you doing today?")

'''
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
'''
me = 'krisHnendu manDal'
print(me.lower())
print(me.upper())
print(me.title())

'''
2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
'''
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

'''
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable 
called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
'''
famous_person = 'albert einstein'
quote = 'A person who never made a mistake never tried anything new.'
message = f'{famous_person.title()} once said, "{quote}"'
print(message)

'''
2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
'''
name = "\n\t   Krishnendu Mandal   \t\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

'''
2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. 
Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this: print(5+3)
Your output should simply be four lines with the number 8 appearing once on each line.
'''
print(6 + 2)
print(9 - 1)
print(4 * 2)
print(8 / 1)

'''
2-9. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. 
Print that message.
'''
my_fav_num = 8
message = f"{my_fav_num} is my favorite number"
print(message)