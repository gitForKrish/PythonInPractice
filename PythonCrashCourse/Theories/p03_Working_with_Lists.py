# -------------------------------------Loop through the entire list--------------------------------
magicians = ['alice', 'david', 'carolina']

for magician in magicians:                              
    print(f"{magician.title()}, that was a great trick!")

#-----------------------------Indenting Unnecessarily After the Loop-------------------------------
for magician in magicians:                              
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    #print("Thank you everyone, that was a great magic show!")
print("Thank you everyone, that was a great magic show!")

#------------------------------- Using the range() Function---------------------------------------
for i in range(10):             # 1st Para is max value (exclusive) 
    print(i)

for i in range(20, 30):         # 1st para is start value (inclusive) & 2nd para is end value (exclusive)
    print(i)

for i in range(40, 50, 2):      # 3rd para is the step
    print(i)

# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

# list of the first 10 square numbers
square = []
for i in range(1,11):
    value = i ** 2
    square.append(value)
print(square)

#-------------------------- Simple Statistics with a List of Numbers----------------------------------
numbers = [1,2,3,4,5,6,7,8,9,0]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#------------------------- List Comprehensions ------------------------------------------------------
square_values = [value ** 2 for value in range(1,11)]
print(square_values)

#--------------------------------Working with Part of a List-----------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Slicing - zero index system
print(players[2:])              # 1st para: starting point (inclusive)
print(players[:2])              # 2nd para: end point (exclusive)
print(players[2:4])             # start(inclusive) & End (exclusive)
print(players[-2:])             # negative indexing
print(players[:-2])             
print(players[0:5:2])           # 3rd para - steps
print(players[ : :2])

for player in players[:3]:
    print(player)

# Copying from a list
fav_foods = ['pizza','burger','chicken','fish','panner']
friend_likes = fav_foods[:]
print(friend_likes)

# Both are list are separate
fav_foods.append('mushroom')
friend_likes.append('mutton')
print(fav_foods)
print(friend_likes)

# if we use = operator for copying list
# both the variable will refer to same list object
fav_color = ['green', 'orange','red']
friend_likes = fav_color

friend_likes.append('yellow')
print(fav_color)
print(friend_likes)

msg = 'hello'
my_msg = msg

my_msg = my_msg + ' and welcome'
print(msg)
print(my_msg)

# Tuple - An immutable list
point = (4,3)
print(point)
print(point[1])
# point[0] = 6 # Error

for val in point:
    print(val)

# Single value tuple
single = (3,)
print(single)

new_point = (10,4)
point = new_point
print(point)