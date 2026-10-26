#. 49. write a program to print result status.
choice = int(input("Enter result status: "))

match choice:
    case 1:
        print("pass")
    case 2:
        print("Fail")
    case 3:
        print("Distinction")
    case _:
        print("Invalid status")