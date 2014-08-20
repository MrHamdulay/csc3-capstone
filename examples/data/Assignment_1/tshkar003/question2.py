#Assignment 1 Question 2
#student number: tshkar003
#program to check validity of of time entered by the user

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

bHours = 0
bMinutes = 0
bSeconds = 0

if (hours<0) or (hours>23):
    bHours = 1
if (minutes<0) or (minutes>59):
    bMinutes = 1
if (seconds<0) or (seconds>59):
    bSeconds = 1
    
if (bHours == 1) or (bMinutes == 1) or (bSeconds == 1):
    print("Your time is invalid.")
else:
    print("Your time is valid.")
    






    