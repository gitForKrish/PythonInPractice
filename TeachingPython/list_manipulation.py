message = "hello"
print(message[0])   # h
print(message[-len(message)])   # h

print(message[-1])  # o
print(message[1:])  # ello
print(message[3:])  # lo
print(message[:2])  # he
print(message[:-1])  # hell
print(message[:])   # hello
print(message[::2])  # hlo

for char in "hello":
    print(char)

print(list(message))

msg1 = message
msg2 = message[:]  # Shallow Copy
print(msg1, msg2)

message = "I have changed"
print(msg1, msg2)
