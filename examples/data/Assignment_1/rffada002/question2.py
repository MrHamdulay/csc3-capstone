hours=input("Enter the hours: \n")
minutes=input("Enter the minutes: \n")
seconds=input("Enter the seconds: \n")

if 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59 and 0 <= int(seconds) <= 59:
        print ("Your time is valid.")
else:
        print ("Your time is invalid.") 