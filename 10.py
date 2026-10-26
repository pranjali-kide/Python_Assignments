# 10. Write a program to check whether a number is a single-digit number or not.
num = int(input("enter a number: "))

if num <= 9:
    print("single digit number")
elif num <= 99:
    print("No is not single digit number")
else:
    print("No is greater than 99")