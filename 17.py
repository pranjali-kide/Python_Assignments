# 17. Write a program to check grade based on marks (A, B, C, fail).
marks = int(input("Enter a marks: "))

if marks >= 80:
    print("Grade = A")
elif marks >= 60:
    print("Grade = B")
elif marks >= 40:
    print("Grade = C")
else:
    print("Fail")