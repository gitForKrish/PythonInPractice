# Python Keywords
import keyword

keywords = keyword.kwlist
print(f"Total python keywords = {len(keywords)}")
print(f"Here are the keyword list:\n{keywords}")

print("*"*100)
# Loops: While-else and For-else
nums = [10, 12, 15]
index = sum = 0
while(index < len(nums)):
    sum += nums[index]
    # if nums[index] == 12:
    #     break
    index += 1
else:
    print('No more items left')
print(f"Sum total = {sum}")

sum = 0
for num in nums:
    sum += num
    # if num == 12:
    #     break
else:
    print('No more items left')
print(f"Sum total = {sum}")
print("*"*100)
