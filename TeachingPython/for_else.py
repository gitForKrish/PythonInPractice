# for - else
sucessful = False
for trying in range(1, 11):  # 0,1,2
    print('Login attempted ' + ('.' * trying))
    # ....
    if sucessful:
        print('Login succeded...')
        break
else:
    print(f"Login attempted {trying} times and failed")

print(trying)
