# 35. Create a list and remove all even numbers.
numbers = [89,68,34,64,76,77,56,67]
result = [n for n in numbers if n % 2 != 0]
print("List without even numbers:", result)