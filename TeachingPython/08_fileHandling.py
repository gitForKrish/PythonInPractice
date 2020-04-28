file = open('08_fileDemo.txt','w')
file.write('This is first line')
file.write('\nThis is second line')
file.close()

file = open('08_fileDemo.txt','r')
print(file.readlines())
file.close()

file = open('08_fileDemo.txt','a')
file.write('\nThis is appended line')
file.close()

file = open('08_fileDemo.txt','r')
print(file.readlines())
file.close()