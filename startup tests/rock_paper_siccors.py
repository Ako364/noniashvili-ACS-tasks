import random

player_choice = input("input either R,P or S : ")

choices = ("Rock", "Paper", "Scissors")
Computers_choice = random.choice(choices)

if Computers_choice == "Rock":

    print(Computers_choice)

    if player_choice == "R":
        print("Tie")
    if player_choice == "S":
        print("Win")
    if player_choice == "P":
        print("Lose")

if Computers_choice == "Paper":

    print(Computers_choice)

    if player_choice == "R":
        print("Lose")
    if player_choice == "S":
        print("Win")
    if player_choice == "P":
        print("Tie")

if Computers_choice == "Scissors":

    print(Computers_choice)

    if player_choice == "R":
        print("Win")
    if player_choice == "S":
        print("Tie")
    if player_choice == "P":
        print("Lose")
