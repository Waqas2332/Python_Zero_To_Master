import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome To PyPassword Generator!!")
letters = int(input("How Many Minimum Letters Would You Like to Add in your Password = "))
numbers = int(input("How Many Numbers Would You Like to Add in your Password = "))
symbols = int(input("How Many Symbols Would You Like to Add in your Password = "))

password = ""
random_loop = 0
total_letters = letters + numbers+symbols

while(total_letters > 0):
    random_loop = random.randint(0,2)
    if random_loop == 0:
        if numbers > 0:
            password = password + numbers_list[random.randint(0,9)]
            numbers = numbers - 1
        else:
            password = password + letters_list[random.randint(0,51)]
    elif random_loop == 1:
        if symbols > 0:
            password = password + symbols_list[random.randint(0,8)]
            symbols = symbols - 1
        else:
            password = password + letters_list[random.randint(0,51)]
    else:
        password = password + letters_list[random.randint(0,51)]
    total_letters = total_letters - 1
print(f"Here is your password : {password}")


