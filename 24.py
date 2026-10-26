# 24. Write a program to check exam result.
marks = int(input("Enter a marks: "))

if marks >= 80:
    print("Distinction")
elif marks >= 60:
    print("First class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")