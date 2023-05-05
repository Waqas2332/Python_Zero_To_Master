import random 

# For Generating a random integer between given range
num = random.randint(1,100)
print(num)

#For generating a random floating number between 0 and 1
num = random.random()
print(num)


# Practice
# Output Head or Tail according to random number
res = ["Heads","Tails"]
num = random.randint(1,2)
print(res[num-1])