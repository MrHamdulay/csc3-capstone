
Hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
Seconds = eval(input("Enter the seconds:\n"))


if 0 <= Hours <= 23 and 0 <= minutes <= 59 and 0 <= Seconds <= 59:
    print("Your time is valid.")
else:

    print("Your time is invalid.")

