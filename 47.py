# 47. Write a program to print language choice.
choice = int(input("Enter language choice: "))

match choice:
    case 1:
        print("English")
    case 2:
        print("Hindi")
    case 3:
        print("Marathi")
    case 4:
        print("Tamil")
    case _:
        print("Invalid choice")
