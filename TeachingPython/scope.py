message = "Hey all"


def greeting():
    msg = 'addi'
    global message
    message = "Good Evening"
    print(message)


def send_email():
    message = "what are you doing?"
    message = 'i am playing now'
    print(message)


greeting()          # RAM - Garbage Colletion
send_email()
print(message)
