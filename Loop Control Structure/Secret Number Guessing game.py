import random
guess_game = '''
=========================================
       Secret Number Guessing Game         
Can you guess the secret number?
Select any number between 1 to 100
See how many tries you take to guess it
=========================================
'''
guess, count, secret = 0, 0, 0
print(guess_game)
secret = random.randint(1, 100)

carry_on = "yes"
while carry_on.lower() == "yes":
    while guess == False:
        guess = int(input("Make a guess between 1 to 100: "))
        #correct guess
        if guess == secret:
            count += 1
            print("Congratulations! You guessed the secret number in", count, "tries!") 
            guess = True
            break
        #wrong guess
        if guess > secret:
            count += 1
            print("The secret number is lower.")
            guess = False
            carry_on = input("would you like to continue?")
        elif guess < secret:
            count += 1
            print("The secret number is higher.")
            guess = False
            carry_on = input("would you like to continue?")

    
    