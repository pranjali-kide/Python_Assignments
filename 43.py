# 43. Write a program for traffic signal using match case.
signal = input("Enter a traffic signal: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("invalid signal")
    