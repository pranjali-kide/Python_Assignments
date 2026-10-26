# write a program to simple ATM menu.

choice = int(input("Enter your chice: "))

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw MOney")
    case 3:
        print("Deposit MOney")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")