hours=input("Enter the hours: \n")
minutes=input("Enter the minutes: \n")
seconds=input("Enter the seconds: \n")

if 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59 and 0 <= int(seconds) <= 59:
    print("Your time is valid.")
elif int(hours)<0 or int(hours)>23 or int(minutes)<0 or int(minutes)>59 or int(seconds)<0 or int(seconds)>59:
    print("Your time is invalid.")