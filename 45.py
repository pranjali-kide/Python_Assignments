# 45. write a program to give grade description using match case.

grade = input("Enter grade: ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("very good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")
