import random


# for i in range(5):
while True:
    choices = ["rock", "paper", "scissor"]

# Initial user input
    user = input("Enter your choice (rock, paper, scissor): ").lower()

# Check if the input is valid
    while user not in choices:
        user = input("Invalid choice. Please enter rock, paper, or scissor: ").lower()
    computer=random.choice(choices)
    # print("computer chose : "+computer)
    if user == computer:
        print("user : "+user)
        print("computer : "+computer)
        print("game is tie")
    elif user =="paper" and computer =="rock":
        print("user : "+user)
        print("computer : "+computer)
        print("user is win")
    elif user =="rock" and computer =="scissor":
        print("user : "+user)
        print("computer : "+computer)
        print("YOU is win")
    elif user=="scissor" and computer=="paper":
        print("user : "+user)
        print("computer : "+computer)
        print("user is win")
    elif user =="rock" and computer =="paper":
        print("YOU : "+user)
        print("computer : "+computer)
        print("computer is win")
    elif user =="scissor" and computer =="rock":
        print("YOU: "+user)
        print("computer : "+computer)
        print("computer is win")
    elif user=="paper" and computer=="scissor":
        print("user : "+user)
        print("computer : "+computer)
        print("computer is win")

    play_again=input("play again (yes/no)? ").lower()
    if play_again != "yes":
        break

print("game is over")

