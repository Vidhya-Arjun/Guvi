#Problem 1: Program to generate random number and user has to guess it
#library used to generate random number
import random
# storing random number in integer x
x = random.randint(1, 10)

#while loop is used for iterating until condition is satisfied
while True:
    #user input is assigned to a variable and in general input method returns string value
    #hence it is converted to integer for numeric comparison
    userInput = int(input("Enter a number: "))
    #condition or loop will execute when the user input is less than random number
    if x < userInput:
        print("Too low! Try again.")
    #condition or loop will execute when the user input is greater than random number
    elif x > userInput:
        print("Too high! Try again.")
    #condition or loop will execute when the user input is equal to random number
    else:
        print(f" Correct! The number was {x}.")
        break  # Exit the loop once correct