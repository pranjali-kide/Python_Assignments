# 37. Create a list and check palindrome list.
numbers = [1,2,3,2,1]
if numbers == numbers[::-1]:
    print("List is palindrome:")
else:
    print("List is not palindrome")