name = "Waqas"
# len() ==> This function is used to calculate the length of the string
length = len(name)
print(length)

# Accesing Strings with range
name[0]
# For accessing a range of characters
print(name[2:4]) # First limit is included, second one is excluded

#String Methods 
#1) lower() / upper() ==> for transforming strings in the lower or upper case respectively

print(name.lower())
print(name.upper())

#count() ==> for counting total number of occurunces of the given substring in the variable. USECASE ==> variable.count("sub-string")
#Return total number of occurunce of given substring in string if found, otherwise it returns -1

print(name.count("a"))
#replace() ==> for replacing any-substring with new substring 
#USECASE ==> variable.replace(what to be replaced , new sub-string)
#It returns new string , doesn't apply any changes to the original string

new_name = name.replace("a","A")
print(new_name)

# string formatting
print(f"Hello {name}")
#dir(variable) ==> returns all the methods and properties that are available on some variable according to the datatype
print(dir(name))