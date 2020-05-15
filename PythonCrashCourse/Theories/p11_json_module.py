import json

numbers = [2, 5, 8, 4, 9, 2, 1, 5, 7, 9, 10]

try:
    with open('p11_json_data.json', 'w') as fp:
        json.dump(numbers, fp)
except:
    pass

try:
    with open('p11_json_data.json', 'r') as fp:
        json_data = json.load(fp)
except FileNotFoundError:
    print('JSON file is not found')
else:
    print(json_data)

file_name = "p11_users.json"
try:
    with open(file_name) as fp:
        username = json.load(fp)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(file_name, 'w') as fp:
        json.dump(username, fp)
    print(f'We will remember you, {username.title()}')
else:
    print(f'Welcome back {username.title()}')
