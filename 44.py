# 45. write a program to manu-based food selection.
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("sandwich")
    case 4:
        print("Pav bhaji")
    case _:
        print("invalid choice")