# 19. Create a list of 10 numbers and remove duplicates.
numbers = [10,20,10,50,20,20,40,80,40]
unique_number = list(dict.formkeys(numbers))

print("Original list:", numbers)
print("Without duplicates:", unique_number)