print('Hello Python World!')

#---------------------------------Variable----------------------------------------------
message = 'Hello Python World!'                 # message - variable
print(message)

message = "Hello Python Crash Course World!"    # variable is changing value
print(message)

message = "Hello Python Crash Course reader!"   # variables as labels that you can assign to values
#print(mesage)                                   # Avoiding Name Errors When Using Variables

#---------------------------------String----------------------------------------------
"This is a string."                             # A string is a series of characters
'This is also a string.'                        # Enclose either with single or double quotes

"He's a good boy"                               # Mixing single and double quotes
'He is a "good" boy'                            # Reversed way
"He's a \"good\" boy"                           # Escaping (\) double quote

"The language 'Python' is named after Monty Python, not the snake."     # String literals

name = "KrisHnendU ManDaL"                      # variable with string value
print(name.title())                             # each word to title case - begins with a capital letter
print(name.upper())                             # string to all uppercase letters
print(name.lower())                             # string to all lowercase letters

first_name = "krishnendu"
last_name = "mandal"
full_name = f"{first_name} {last_name}"         # F-stirng or formatted-string (F-strings were introduced in Python 3.6)
                                                # Python 3.5 or before, need to use the format() method as below
                                                # full_name = "{} {}".format(first_name, last_name)
print(full_name)                                # Replace the name of the variables including braces with it's value
print(f"Hello, {full_name.title()}")

print("Languages:\n\tPython\n\tC\n\tC#")        # Adding Whitespace to Strings with Tabs or Newlines

fav_lang = " python "                           # Stripping Whitespace - Removing extra white space from both ends
print(fav_lang.rstrip())                        # rstrip() - Remove whitespace from right side
print(fav_lang.lstrip())                        # lstrip() - Remove whitespace from left side
print(fav_lang.strip())                         # strip() - Remove whitespace from both side

print(type(fav_lang))                           # type() - Return the underlaying data type

#---------------------------------Number----------------------------------------------
# Integers
print(2 + 3)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)                                   # // - Floor division
print(3 % 2)                                    # % - Remainder/Modulus
print(3 ** 2)                                   # ** - Exponent
print(3 + 2 * 4)
print((3 + 2) * 4)
print(type(10))

# Floats
print(0.2 + 0.1)                                # sometimes you may get an arbitrary number of decimal places like 0.3000000000004
print(0.2 * 2)

# Python defaults to a float in any operation that uses a float, even if the output is a whole number
print(1 + 2.0)
print(2 * 3.0)
print(2.0 ** 3)
print(4 / 2)

universe_age = 14_000_000_000                   # Underscore for more readablity (Available from Python 3.6)
print(universe_age)                             # 1000 same as 1_000 and 10_00

x,y,z = 0,0,0                                   # Multiple assignments
