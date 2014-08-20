Hrs = int(input("Enter the hours: \n"))
Min = int(input("Enter the minutes: \n"))
Sec = int(input("Enter the seconds: \n"))
if Hrs <= 23 and Hrs >= 0:
    if Min <= 59 and Min >= 0:
        if Sec <= 59 and Sec >= 0:
            print("Your time is valid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
else:
    print("Your time is invalid.")
