# from prime import isPrime as ip, sayHello as sh
# import prime as pm

# x = int(input("Enter a number:"))
# print(pm.isPrime(x))
# sh()

# x = int(input("Enter a number:"))
# print(ip(x))

a = 10
long_str = F"""
This is my own string blah blah blah!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    Hello 
                            this {5+5}
                    is {a}
            a
                            long string
                    """

print(long_str)

print(bool(0))  # False
print(bool(20))  # True
print(bool(-20))  # True
print(bool(True))  # True
print(bool(False))  # False
print(bool("True"))  # True
print(bool("False"))  # True
print(bool(""))  # True/false
var1 = (10,)
print(bool(var1))  # True
print(bool([]))  # False
print(bool(None))  # False
print(bool(5+2-7))  # False


# Falsy - Absence of value - zero, empty string, None, empty list,set,dictionary
# Truthy - Presence of value

print(ord("@"))
