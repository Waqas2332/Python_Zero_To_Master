# from replit import clear

auction_data = {}
isContinue = True
print("Welcome to Secret Auction Program")
while(isContinue):
    name = input("\nWhat's your name : ")
    bid = int(input("\nWhat's your bid : $"))
    auction_data[name] = bid
    isOver = input("\nAre there any other bidders ? Type 'yes' or 'no'. ") 
    if(isOver == 'yes'):
        continue
    else:
        break  

print(auction_data)
maxAuc = 0
winner = ""
for data in auction_data:
    amount = auction_data[data]
    if amount > maxAuc:
        maxAuc = amount
        winner = data

print(f"The Winner is {winner} with bid of {maxAuc}")