print('Reading file contents using OPEN & With block')
# Using relative path
filename = 'p09_pi_digits.txt'
with open(filename) as file_obj:
    contents = file_obj.read()
print(contents)

# Using absolute path
with open('C:/Users/ADMIN/Documents/PythonInPractice/PythonCrashCourse/Theories/p09_pi_digits.txt') as file_obj:
    contents = file_obj.read()
print(contents)

print('\nReading file content line by line -->')
with open(filename) as file_object:
    for line in file_object:
        # each line is having \n and print adds another \n, thus two new lines will appear in console
        print(line)

print('\nMaking list of lines from the file -->')
with open(filename) as file_obj:
    lines = file_obj.readlines()
for line in lines:
    print(line.rstrip())    # rstrip() will remove \n from each line

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
