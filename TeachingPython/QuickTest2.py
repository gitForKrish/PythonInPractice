'''
2-1. Simple Message: Assign a message to a variable, and then print that message.
'''
message = 'good evening'
print(message)              # good evening
print(message.title())      # Good Evening


msg = "how are yOu? hope eVeyThing is good!"
# Pascal Case
print(msg.title())          # How Are You? Hope Eveything Is Good!

# Upper Case
print(msg.upper())          # HOW ARE YOU? HOPE EVEYTHING IS GOOD!

# Lower Case
print(msg.lower())          # how are you? hope eveything is good!

# Camel Case
# numberOfStudents

'''
2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new message.
'''
message = "How are you?"
print(message)

message = "I am fine"
print(message)

'''
2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
'''
name = 'purnendu mandal'
print(name + " ,would you like to learn some Python today?")            # purnendu mandal ,would you like to learn some Python today?
print(name.title() + " ,would you like to learn some Python today?")    # Purnendu Mandal ,would you like to learn some Python today?

'''
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
'''
person_name = "Jack"
print(person_name.lower())
print(person_name.upper())
print(person_name.title())
'''
2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
'''
print("Rabindranath Tagore once said,\"Where the mind is without fear, where the head is held high\"")
# Rabindranath Tagore once said,"Where the mind is without fear, where the head is held high"
print('Rabindranath Tagore once said,"Where the mind is without fear, where the head is held high"')

'''
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable 
called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
'''
famous_person = "Rabindranath Tagore"
message = 'once said,"Where the mind is without fear, where the head is held high"'
print(famous_person + message) # Rabindranath Tagoreonce said,"Where the mind is without fear, where the head is held high"
print(famous_person + " " + message) # Rabindranath Tagore once said,"Where the mind is without fear, where the head is held high"
print(famous_person, message) # Rabindranath Tagore once said,"Where the mind is without fear, where the head is held high"

name = 'purnendu'
print("Hello " + name)
print(f"Hello {name}")

#print(famous_person + "message")
print(f"{famous_person} {message}") # Rabindranath Tagore once said,"Where the mind is without fear, where the head is held high"

'''
2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once. 
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
'''
name = "     \t\n Michel Jackson\n\n\t     "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
'''
2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. 
Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this: print(5+3)
Your output should simply be four lines with the number 8 appearing once on each line.
'''
print(6 + 2)    # 8
print(10 - 2)   # 8
print(4 * 2)    # 8
print(24 // 3)  # 8
'''
2-9. Favorite Number: Use a variable to represent your favorite number. 
Then, using that variable, create a message that reveals your favorite number. Print that message.
'''
fav_number = 8
message = f"{fav_number} it is enclosed totally"
print(message)                      # 8 it is enclosed totally

message = "it is enclosed totally"
print(f"{fav_number} {message}")    # 8 it is enclosed totally

