nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []

#? Creating List with loops
for n in nums:
    my_list.append(n)
    
print(my_list)

# ? Creating same list with list comprehension
my_list = [n for n in nums]
print(my_list)

# TODO creating a list where all even elements from nums is present 
my_list = []

# ? using loops
for n in nums:
    if n%2 == 0:
        my_list.append(n)
        
print(my_list)

# ? using list comprehension
my_list = []
my_list = [n for n in nums if n%2 == 0]
print(my_list)


# TODO create list with pairs like this a,0 a,1 a,2 a,3 b,1 b,2 ... d3

# ? using loops
my_list = []
alpha = ["a","b","c","d"]
for letter in alpha:
    for i in range(4):
        my_list.append((letter,i))
        
print(my_list)


# ? using list comprehension
my_list = []

my_list = [(letter,i) for letter in alpha for i in range(4)]
print(my_list)