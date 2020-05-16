from ut_01_namefunc import get_formatted_name

print('Info: Press "q" to quit anytime\n')
while True:
    first = input('First Name: ')
    if first == 'q':
        break
    last = input('Last Name: ')
    if last == 'q':
        break
    full_name = get_formatted_name(first, last)
    print(f"{full_name} \n")