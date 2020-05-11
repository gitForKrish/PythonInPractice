def greet_user():
    """ Message for greeting """
    print('hello')

greet_user()

def greet_user(name):
    """ Message for greeting """
    print(f'hello, {name.title()}')

greet_user('jack')
# greet_user()      # TypeError: greet_user() missing 1 required positional argument: 'name'

def describe_animal(animal_type, pet_name):
    ''' Method will describe an animal '''
    print(f"I have a {animal_type.title()}")
    print(f"My {animal_type.title()} name is {pet_name.title()}")

# Positional Arguments
describe_animal('dog', 'jack')

# Keywords Arguments
describe_animal(animal_type='cat', pet_name='buli')
describe_animal(pet_name='tommy', animal_type='dog')

# default value
def describe_animal(pet_name, animal_type = 'dog'):
    ''' Method with default arguments '''
    print(f"I have a {animal_type.title()}")
    print(f"My {animal_type.title()} name is {pet_name.title()}")

describe_animal('kalu')
describe_animal('supert', 'tiger')
describe_animal(animal_type='cat',pet_name='lione')

# Function returning value
def get_formatted_name(first_name, last_name):
    ''' Get Formatted Name '''
    return f"{first_name.title()} {last_name.title()}"

my_name = get_formatted_name('krishnendu', 'mandal')
print(my_name)

def get_formatted_name(first_name, last_name, middle_name=''):
    ''' Get Formatted Name '''
    full_name = ''
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

my_name = get_formatted_name('krishnendu', 'mandal')
print(my_name)

father_name = get_formatted_name('tarun','mondal','kumar')
print(father_name)