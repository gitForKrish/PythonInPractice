# 9. List out  all the odd numbers from 1 to 100 using lists in Python.
# oddNumbers = [i for i in range(1,100,2)]
# print(oddNumbers)
# oddNumbers = []
# for i in range(1,100,2):
#     oddNumbers.append(i)
#     #print(oddNumbers) #[1], [1,3], [1,3,5] ... [99]
# print(oddNumbers)

oddNumbers = []
for i in range(1, 100, 2):
    oddNumbers.append(i)
print(oddNumbers)

print()
oddNumbers = list(range(1, 100, 2))
print(oddNumbers)

print()
# list comprehension
oddNumbers = [i*i for i in range(1, 100, 2)]
print(oddNumbers)

sentence = "This is a interview questions"
# char_list = [*sentence]
# print(char_list)

# char_freq = {ch: sentence.count(ch) for ch in char_list}
# print(char_freq)

# highest_frequently_used = sorted(
#     char_freq, key=lambda item: char_freq[item], reverse=True)[0]
# print(highest_frequently_used)

char_freq = {ch: sentence.count(ch) for ch in sentence}
most_used = sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True)[0]
print(*most_used)
