hours=input("Enter the hours: \n")
minutes=input("Enter the minutes: \n")
seconds=input("Enter the seconds: \n")
if 0<=eval(hours)<=23 and 0<=eval(minutes)<=60 and 0<=eval(seconds)<=60:
    print("Your time is valid.")
else:
    print("Your time is invalid.")