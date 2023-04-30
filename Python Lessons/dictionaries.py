new_dict = {
    "name":"Waqas",
    "age":12,
    "hobbies":["Code","Code","Code"]
}

# Accessing elements from dict
# Below method is use to access the value of key but it will throw error if key is not present
print(new_dict["age"])
# get(key,default message) ==> returns value if found else returns None or default message if it is set
print(new_dict.get("kuch bhi"))
print(new_dict.get("kuch bhi","Key Not Found"))


# Updating Dictionaries
new_dict["earnings"] = 0
print(new_dict)
# If you want to update more than one item than use 
# update(dict)
new_dict.update({
    "age":20,
    "phone":"03000000"
})
print(new_dict)



# Deleting From dictionaries
# del keyword ==> del dict[key] ==> it will delete the key value pair from dictionary
del new_dict["earnings"]
print(new_dict)
# pop(key) ==>  it will delete the given key from dictionary as well as return its value
phone = new_dict.pop("phone")
print(new_dict)
print(phone)


# LOOPING from dictionaries
# items() ==> returns key,values in the form of pairs
print(new_dict.items())
for key,value in new_dict.items():
    print(key,value)



# Some Else dictionary methods
# len(dict) ==> returns total number of keys in dictionary
print(len(new_dict))
# key() ==> returns all the keys of dictionary
print(new_dict.keys())
# values() ==> returns all the values of dictionary
print(new_dict.values())