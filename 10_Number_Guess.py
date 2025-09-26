import random
num = random.randint(1, 100)
guess = 0
while guess != num:
    guess = int(input("Choose a number from 1 to 100 : "))
    if(guess > num):
        print("Too high! You Guessed Wrong.")
    elif(guess < num):
        print("Too low! You Guessed Wrong.")
    else:
        print("Congratulations! You Guessed Right.")