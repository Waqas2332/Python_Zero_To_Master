import random

word_list = ["aardvark", "baboon", "camel"]

#? - Randomly Choosing a word from list

chosen_word = random.randint(0,2)


# ? Generating an underscore lists , underscores will be equal to number of letters in choosen word

underscore_list = []
for i in word_list[chosen_word]:
    underscore_list.append("_")



print("Welcome To PyGuess Game!\nYou have to Guess a word in 10 tries\nGood Luck!!\n")

#? Checking whether user guessed or not
total_guess = 10
while(total_guess):
    # ? Taking Guess From User
    guess = input("Guess a letter : ").lower()
    
    # ? Checking User input
    for idx,chr in enumerate(word_list[chosen_word]):
        if chr == guess:
            underscore_list[idx] = chr
    print(underscore_list)
    print("\n")
    total_guess = total_guess - 1
    if "_" in underscore_list:
        print(f"\nYou have {total_guess} tries left!")
        continue
    else:
        print("You Win")
        break
    print(f"\nYou have {total_guess} tries left!")

if "_" in underscore_list:
    print(f"You Lose!!\nWord was {word_list[chosen_word]}\nBetter Luck Next Time")
else:
    print("Congratulations!!!")
