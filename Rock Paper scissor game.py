"""
WORKFKOW OF PEOJECT:
1 - Input from user (Rock, Paper, Scissor)
2 - computer choice (Computer will choose randomly not conditionally)
3 - Rsults print

cases:

A - Rock
Rock - Rock = Tie
Rock - Papere =  Paper win
Rock - Scissor = Rock win

B - Paper
Paper - Paper = Tie
Paper - Rock  = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor - Scissor = Tie
Scissor - Rock = Rock win
Scissor -  Paper = Scissor win

"""

import random

item_list = ["Rock", "Paper", "scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
 
if user_choice == comp_choice:
    print("Both chooses same: Match Tie")


elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")


elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer win")
    else:
        print("Paper covers Rock, You win")


elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Scissor cuts Paper, Computer win")
    else:
        print("Rock smashes Scissor, You win")

        