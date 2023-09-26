"""Guess the sum of 2 dice!"""
from random import randint
from time import sleep

def roll_dice(num_sides_1, num_sides_2):
    #rolling dice up to the max dice face
    #global the variables(first_roll, second_roll and max_val) so its usable in get_user_guess()
    global first_roll
    first_roll = randint(1, num_sides_1)
    global second_roll
    second_roll = randint(1, num_sides_2)
    global max_val
    max_val = num_sides_1 + num_sides_2
    print("Rolling...")
    sleep(1) #Pauses the program for sleep(seconds)

def get_user_guess():
    guess_counter = 1
    guess = 0
    guessloop = False
    while guessloop == False:
        guess = int(input(f'''Attempt: {guess_counter}
Make your guess: '''))
        #guess > max_val arguement first so input over the maximum will not be caught by guess 1= rolled_val arguement
        if guess > max_val:
            guess_counter += 1
            print(f'''Max roll: {max_val}
You have gone over the max roll. 
Try something smaller.''')
        elif guess != rolled_val:
            guess_counter += 1
            print("Try again!")
            roll_dice(num_sides_1, num_sides_2)
        elif guess == rolled_val:
            print(f"Congratulations! You have guessed the dice numbers in {guess_counter} attempts!")
            guessloop = True

num_sides_1 = int(input("Enter number of sides of 1st die: "))
num_sides_2 = int(input("Enter number of sides of 2nd die: "))
roll_dice(num_sides_1, num_sides_2)
rolled_val = first_roll + second_roll
get_user_guess()