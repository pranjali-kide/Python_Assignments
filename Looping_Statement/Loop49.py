# 49. Display menu-driven program using while loop.
while True:
    print("\n----MENU----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice (1-5):")

    if choice == "5":
        print("Goodbye!")
        break
    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice, try again.")
        continue

    a = float(input("Enter First number: "))
    b = float(input("Enter Second number: "))
    if choice == "1":
        print("Result =",a + b)
    elif choice == "2":
        print("Result =",a - b)
    elif choice == "3":
        print("Result =",a * b)
    else:
        print("Result =",a/b if b != 0 else "Cannot divide by zero")


if __name__ == "__main__":
    interactive = {36, 37, 49}
    for k in range(1,50):
        if k in interactive:
            continue
        print(f"\n====Question {k} ====")
        globals()[f"q{k}"]()
