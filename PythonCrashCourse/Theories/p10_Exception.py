# handle Zero Division Error
try:
    print(5/0)
except:
    print('Divison by Zero occurred')

# Many times division
print('\nGive me two numbers. I will try to devide ->')
print('Info: Press "q" to exit anytime')

while True:
    first = input('Enter 1st number: ')
    if first == 'q':
        break
    second = input('Enter 2nd number: ')
    if second == 'q':
        break

    try:
        result = int(first)//int(second)
    except ZeroDivisionError:
        print('Division by zero is not possible\n')
    except ValueError:
        print('Division is only possible for numeric number\n')
    else:
        print(f'Division = {result}\n')

'''
10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. 
Catch the ValueError if either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text instead of a number.
'''
print('\nGive me two numbers. I will try to add:')
print('Info: Press "q" to quit anytime')
while True:
    first_num = input('First Number = ')
    if first_num == 'q':
        break
    second_num = input('Second Number = ')
    if second_num == 'q':
        break

    try:
        result = int(first_num) + int(second_num)
    except ValueError:
        print('Addition is only possible with numeric values\n')
    else:
        print(f"Addition = {result}\n")

'''
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and
enter text instead of a number. 
'''

'''
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. 
Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
executes properly.
'''
try:
    with open('p10_exception_cats.txt') as file_cat:
        cat_contents = file_cat.read()
    with open('p10_exception_dogs.txt') as file_dog:
        dog_contents = file_dog.read()
except FileNotFoundError:
    print('Unable to access the file path')
else:
    print(cat_contents)
    print(dog_contents)
'''
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.
'''

''' 
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ ) and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your computer. You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:
  line = "Row, row, row your boat"
  line.count('row') -> 2
  line.lower().count('row') -> 3
Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.
Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.
'''
