# 30. Write a program to check the type of number. (single, double, triple)
num = int(input("Enter a number: "))

if num <= 9:
    print("Single digit number")
elif num <= 99:
    print("Double digit number")
else:
    print("Three digit number")