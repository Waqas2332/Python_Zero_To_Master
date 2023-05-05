import random

choices = ["Rock","Paper","Scissors"]

user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper & 2 for Scissors = "))

if(user_choice > 2):
    print("Invalid Choice")
else:
    comp_choice = random.randint(0,2)
    if user_choice == comp_choice:
        print(f"You Chooses {choices[user_choice]}\nComputer Chooses {choices[comp_choice]}\nDraw!!!")
    elif (user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 0):
        print(f"You Chooses {choices[user_choice]}\nComputer Chooses {choices[comp_choice]}\nComputer Wins!!!")
    else:
        print(f"You Chooses {choices[user_choice]}\nComputer Chooses {choices[comp_choice]}\nYou Wins!!!")
