#question 2
hour=eval(input("Enter the hours:\n"))
minute=eval(input("Enter the minutes:\n"))
second=eval(input("Enter the seconds:\n"))

if 0<=hour<=24:
    if 0<=minute<=59:
        if 0<second<=59:
            print("Your time is valid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
else:
    print("Your time is invalid.")