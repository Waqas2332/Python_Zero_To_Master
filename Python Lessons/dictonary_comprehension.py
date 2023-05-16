nums = [0,1,2,3]
alpha = ["a","b","c","d"]

# TODO creating dictonary comprehension from two lists

# ? using loops
my_dict = {}
for n,a in zip(nums,alpha):
    my_dict[n] = a

print(my_dict)

#  ? using dictionary comprehension
my_dict = {}
my_dict = {n:a for n,a in zip(nums,alpha)}
print(my_dict)

# ? using conditionals in dictionary comprehension
my_dict = {}
my_dict = {n:a for n,a in zip(nums,alpha) if n != 0}
print(my_dict)
