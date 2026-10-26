# 36. Create a list and remove all odd numbers.
numbers = [1,2,3,4,5,6,7,8,9,10]
result = [n for n in numbers if n % 2 == 0]
print("List without odd numbers:", result)