	# 9. List out  all the odd numbers from 1 to 100 using lists in Python.
	# oddNumbers = [i for i in range(1,100,2)]
	# print(oddNumbers)
	# oddNumbers = []
	# for i in range(1,100,2):
	#     oddNumbers.append(i)
	#     #print(oddNumbers) #[1], [1,3], [1,3,5] ... [99]
	# print(oddNumbers)

oddNumbers = []
for i in range(1,100,2):
    oddNumbers.append(i)
print(oddNumbers)

print()
oddNumbers = list(range(1,100,2))
print(oddNumbers)

print()
# list comprehension
oddNumbers = [i*i for i in range(1,100,2)]
print(oddNumbers)