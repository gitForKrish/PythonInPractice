age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# cond? truthy:falsy

age = 32
if 18 <= age < 65:
    print("Eligible")


def muliply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(muliply(2, 3, 4, 5, 6))
print(muliply(2, 3, 4, 5, 6, 7, 8, 9))


def showUserDetails(**info):
    # fname = info["firstname"]
    # print(fname)
    # lname = info["lastname"]
    # print(lname)
    print(f"{info['firstname']} {info['lastname']}")


showUserDetails(firstname="John", lastname="Stanley")
