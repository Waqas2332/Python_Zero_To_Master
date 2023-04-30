course = ["Arts","Maths","Science","Computer"]

# len() ==> returns the length of list
print(len(course))

# -1 index ==>   always returns the last element in the list

print(course[-1])

# Modifiying Lists
# append(element) ==> adds element at the end of list
course.append("Chemistry")
# insert(index,element) ==> adds element at given index
course.insert(0,"Physics")
# extend(list) ==> insert the items of list at the end of main list
sec_course = ["Urdu","English"]
course.extend(sec_course)
print(course)
# remove(element) ==> removes the given element from list
course.remove("Chemistry")
print(course)
# pop() ==> remove last element from list and also returns that element
last = course.pop()
print(last)


# Sorting IN Lists
nums = [5,8,3,1,9]
# reverse() ==> reverses the whole list
nums.reverse()
print(nums)
# sort() ==> sort lists in ascending order
nums.sort()
print(nums)
# sort(reverse=True) ==> for sorting in descending order
nums.sort(reverse=True)
print(nums)
# For returning the new sorted list... sorted(list)
sorted_list = sorted(nums)
print(sorted_list)



# Finding Values in Lists
# index(element) ==> if element is present it will return the element otherwise it will throw error
print(nums.index(3))
# IN operator ==> for checking wether element is in the list or not. Returns true/false according to situation
print(3 in nums)
print(2 in nums)




# LOOPING in lists
# Simple for loop
for element in nums:
    print(element)

# If you want to get index with elemenets as well
for idx,element in enumerate(nums):
    print(idx,element)

# you can also specify the starting index in enumerate function
for idx,element in enumerate(nums,start=2):
    print(idx,element)





# Converting List in Strings
# string = seperator.join(list) ==> sperator can be anything like space,comma,hyphen etc
list_str = '-'.join(course)
print(list_str)


# Converting strings in lists
# list = str.split(seperator)
list_new = list_str.split("-")
print(list_new)