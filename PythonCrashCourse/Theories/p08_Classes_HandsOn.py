from time import gmtime, strftime
'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
'''
class Restaurent():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"Welcome to {self.restaurant_name.title()}. This is a {self.cuisine_type.upper()} restaurant!!!")

    def open_restaurant(self):
        current_time = strftime('%H:%M', gmtime())
        if current_time > '11:00' and current_time < '23:00':
            print('Restaurant is open now ...')
        else:
            print('Restaurent is currently closed!!!')

    def set_number_served(self, count):
        self.number_served = count

    def increment_number_served(self):
        self.number_served += 1


my_restaurent = Restaurent('Royal Blues', 'Cuisine')
my_restaurent.describe_restaurant()
my_restaurent.open_restaurant()

'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''
royal_bangla = Restaurent('royal bangla', 'dinning')
royal_mumbai = Restaurent('royal maratha', 'special')
royal_kannada = Restaurent('royal karnataka', 'daily')
royal_bangla.describe_restaurant()
royal_mumbai.describe_restaurant()
royal_kannada.describe_restaurant()

'''
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''
class User():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Name: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}. Hope you are doing good.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('jack', 'william')
user2 = User('michel', 'stanley')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

'''
9-4. Number Served: Start with your program from Exercise 9-1.
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
'''
restaurant = Restaurent('Banglar Shaad', 'General')
print(f"Nuber of customer served = {restaurant.number_served}")
restaurant.number_served = 10
print(f"Nuber of customer served = {restaurant.number_served}")

restaurant.set_number_served(25)
print(f"Nuber of customer served = {restaurant.number_served}")

restaurant.increment_number_served()
print(f"Nuber of customer served = {restaurant.number_served}")

'''
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 . Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''
custom_user = User('Tommy', 'Gill')
custom_user.increment_login_attempts()
custom_user.increment_login_attempts()
custom_user.increment_login_attempts()
print(f"Login attempted: {custom_user.login_attempts}")
custom_user.reset_login_attempts()

print(f"Login attempt reset: {custom_user.login_attempts}")

'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 or Exercise 9-4. Either version of the class will work; 
just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
'''
class IceCreamStand(Restaurent):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


ice_cream_stand = IceCreamStand('IceCreamStand', 'Ice Cream Stand', [
                                'Vanilla', 'buttersotch', 'almondcrumble'])
ice_cream_stand.show_flavors()

'''
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
'''
print("------------------------------------------------------------------------------------------")
class User():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Name: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}. Hope you are doing good.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, fname, lname, privileges):
        super().__init__(fname, lname)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


admin_user = Admin('Super', 'Admin', ["can add post", "can delete post", "can ban user"])
admin_user.show_privileges()
print("------------------------------------------------------------------------------------------")

'''
9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
'''
print("------------------------------------------------------------------------------------------")
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('List of privileges:')
        print(self.privileges)

class User():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Name: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}. Hope you are doing good.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, fname, lname, privileges):
        super().__init__(fname, lname)
        self.privileges = Privileges(privileges)


admin_user = Admin('Super', 'Admin', ["can add post", "can delete post", "can ban user"])
admin_user.privileges.show_privileges()
print("------------------------------------------------------------------------------------------")

'''
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''
from random import randint
class Die():
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))

six_sided_die = Die(6)
for i in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.roll_die()
'''
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters. 
Randomly select four numbers or letters from the list and print a message saying that 
any ticket matching these four numbers or letters wins a prize.
'''
from random import choice
mylist = (1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E')
build_ticket = ''
build_ticket += str(choice(mylist))
build_ticket += str(choice(mylist))
build_ticket += str(choice(mylist))
build_ticket += str(choice(mylist))
print(f'Winning Ticket Number: {build_ticket}')

'''
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
'''