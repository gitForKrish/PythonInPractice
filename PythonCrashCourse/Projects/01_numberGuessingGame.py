'''
I'm thinking of a number! 
Try to guess the number I'm thinking of: 25
Too low! Guess again: 50
Too high! Guess again: 42
That's it! Would you like to play again? (yes/no) no
Thanks for playing!
'''
import random
print("I'm thinking of a number between 0 to 100!")
number = random.randint(0,100)
guessNum = int(input("Try to guess the number I'm thinking of: "))
repeat = True
noOfGuess = 0
while(repeat):    
    noOfGuess += 1
    if number == guessNum:
        print("Congratulation, You have guessed the right!")
        print("Would you like to play again? (yes/no)", end=" ")
        if input() == "yes":
            noOfGuess = 0
            guessNum = int(input("Try to guess the number I'm thinking of: "))
        else:
            repeat = False
            
    elif number > guessNum:
        print('Too low! Guess again:', end=" ")
        guessNum = int(input())
        noOfGuess += 1
    else:
        print('Too high! Guess again:', end=" ")
        guessNum = int(input())
        noOfGuess += 1

    if noOfGuess == 5:
        print("That's it! Would you like to play continue? (yes/no)", end=" ")
        if input() == "yes":
            noOfGuess = 0            
        else:
            repeat = False

print('Thanks for playing!')
