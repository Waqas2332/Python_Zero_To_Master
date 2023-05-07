alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

isOver = True

def encrypt(message,shift):
    for idx,chr in enumerate(message):
        if chr == " ":
            message = message + chr
            continue
        index = alphabet.index(chr)
        index = index + shift
        if(index > 25):
            index = index - 26
        message =  message.replace(chr,alphabet[index])
    return message
        
def decrypt(message,shift):
    for chr in message:
        if chr == " ":
            continue
        index = alphabet.index(chr)
        index = index - shift
        if(index < 0):
            index = index + 26
        message = message.replace(chr,alphabet[index])
    return message


while(isOver):
    operation = input("\nType 'encode' to encrypt , type 'decode' to decrypt : ")
    message = input("\nEnter Your Message = ")
    shift = int(input("\nEnter Shift Number = "))
    if(operation.lower() == "encode"):
        message = encrypt(message,shift)
        print(f"Your Encoded Message : {message} ")
    elif(operation.lower() == "decode"):
        message = decrypt(message,shift)
        print(f"Your decoded text : {message}")
    else:
        print("Invalid Option!!! Try Again")
    over = input("Type 'yes' if you want to go again. Otherwise type 'no' : ")
    if(over == 'yes'):
        continue
    else:
        break