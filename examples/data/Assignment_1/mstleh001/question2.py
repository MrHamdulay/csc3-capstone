def time(hours,minutes,seconds):
    if 0<=minutes<=60 and 0<=seconds<=60 and 0<=hours<=23:
        print("Your time is valid.")
    else:
        print("Your time is invalid.\n")
hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
time(hours,minutes,seconds)