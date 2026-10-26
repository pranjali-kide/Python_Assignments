# 34. Create a list and find common element between two lists.
list1 = [67,89,34,78,23,45]
list2 = [89.45,89,12,34,67]

common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)