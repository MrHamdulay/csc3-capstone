#MTHKHI001
#Question2 

hours = int(input("Enter the hours:"))
print("")
minutes = int(input("Enter the minutes:"))
print("")
seconds = int(input("Enter the seconds:"))
print("")

if  hours <= 24 and hours >= 0 and  minutes <= 60 and minutes >= 0 and  seconds <= 60 and seconds >= 0:
    print("Your time is valid.")
else :
    print("Your time is invalid.")