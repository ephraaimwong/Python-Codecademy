from random import *
prompt = ('''Select from the following:
Rock
Paper
Scissors
''')

options = ["Rock", "Paper", "Scissors"]

message = {
  "tie" : "It's a tie!",
  "win" : "You wow the bot!",
  "lose" : "You just lost to a bot?!?!"
}

def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("Computer selected: %s" % computer_choice)
  if user_choice.lower() == computer_choice.lower():
    print(message["tie"])
  elif user_choice.lower() == "rock" and computer_choice.lower() == "scissors":
    print(message["win"])
  elif user_choice.lower() == "paper" and computer_choice.lower() == "rock":
    print(message["win"])
  elif user_choice.lower() == "scissors" and computer_choice.lower() == "paper":
    print(message["win"])
  else:
    print(message["lose"])

def play_RPS():
  user_choice = input(prompt)
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()