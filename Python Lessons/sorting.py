li = [2,3,5,8,1,0,9]

# TODO sorting using sorted function
sorted_li = sorted(li)
print(sorted_li)

# TODO in-place sorting
li.sort()
print(li)


# TODO sorting in descending order
sorted_lis = sorted(li,reverse=True)
print(sorted_lis)
li.sort(reverse=True)
print(li)

# TODO sorting absolute values
nums = [-4,-3,-1,2,4,5,6]
sorted_nums = sorted(nums,key=abs)
print(sorted_nums)