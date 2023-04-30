new_set = {1,2,2,3,4,5,3,7}
print(new_set)

another_set = {2,5,9}

# Sets Methods 
# intersection(set) ==> return common elements from both sets
print(new_set.intersection(another_set))
# union(set) ==> return distinct elements from both sets
print(new_set.union(another_set))
# difference() ==> returns elements that are not present in second set
print(new_set.difference(another_set))