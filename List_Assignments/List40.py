# 40. Create a list and demonstrate all list methods
numbers = [30,10,20,10]

#1. append()
numbers.append(40)
print("append:", numbers)

# 2. extend()
numbers.extend([50,60])
print("extend:",numbers)

# 3. insert()
numbers.insert(1, 15)
print("insert:",numbers)

# 4. removed()
numbers.remove(10)
print("remove:",numbers)

# 5. pop()
numbers.pop()
print("pop:", numbers)

# 6. index()
print("index:", numbers.index(20))


# 7. count()
print("count:", numbers.count(10))

# 8. sort()
numbers.sort()
print("sort:", numbers)

# 9. reverse()
numbers.reverse()
print("reverse:", numbers)


# 10. copy()
new_list = numbers.copy()
print("copy:", new_list)


# 11. clear()
new_list.clear()
print("clear:", new_list)
