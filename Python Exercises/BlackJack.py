from random import randint
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
comp_cards = []
choice = input("Do you want to play a game of Blackjack ? Type 'y' or 'n' : ")

def userTake():
    user_cards.append(card[randint(0,12)])
    return user_cards

def compTake():
    comp_cards.append(card[randint(0,12)])
    return comp_cards

def result(user_cards,comp_cards):
        print(f"Your Final Hand : {user_cards}")
        print(f"Computer Final Hand : {comp_cards}")
        if sum(user_cards) > sum(comp_cards):
            print("You Win")
        elif sum(user_cards) < sum(comp_cards):
            print("Computer Wins")
        else:
            print("Draw")


user_cards = userTake()
comp_cards = compTake()
if(choice == "y"):
    user_cards = userTake()
    comp_cards = compTake()
    print(f"Your Cards : {user_cards}")
    print(f"Computer's First Card : {comp_cards[0]}")
    choice = input("Type 'y' to get another card ,type 'n' to pass : ")
    if choice == 'n':
        result(user_cards,comp_cards)
    elif(choice == "y"):
        user_cards = userTake()
        print(f"Your Cards : {user_cards} , current score : {sum(user_cards)}")
        if(sum(user_cards) > 21):
            print("You went Over 21\nYou Lose")
        elif sum(comp_cards) < 16:
            comp_cards = compTake()
            result(user_cards,comp_cards)
        else:
            result(user_cards,comp_cards)
    