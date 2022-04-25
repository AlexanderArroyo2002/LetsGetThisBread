import random

print("Hello! This is rock paper scissors. You know the drill.")

def playerRock(x):
    choice = random.choice(x)
    if choice == "rock":
        print("I choose rock!")
        print("We tied")
    elif choice == "paper":
        print("i choose paper!")
        print("You lose")
    else:
        print("I choose sciossors!")
        print("You win")

def playerPaper(x):
    choice = random.choice(x)
    if choice == "rock":
        print("I choose rock!")
        print("You win")
    elif choice == "paper":
        print("I choose paper!")
        print("We tied")
    else:
        print("I choose sciossors!")
        print("I win")    

def playerScissors(x):
    choice = random.choice(x)
    if choice == "rock":
        print("I choose rock!")
        print("You lose")
    elif choice == "paper":
        print("I choose paper!")
        print("You win")
    else:
        print("I choose sciossors!")
        print("We tied") 

def main():
    choices = ["rock", "paper", "scissors"]
    answer = input("What is your choice? (rock, paper, or scissors): ")
    if answer == "rock":
        playerRock(choices)
    elif answer == "paper":
        playerPaper(choices)
    elif answer == "scissors":
        playerScissors(choices)
    else:
        print("Invalid answer. Please retry")
        main()
main()
    
