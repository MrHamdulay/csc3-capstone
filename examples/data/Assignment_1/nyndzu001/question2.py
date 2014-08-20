#Author: Dzunisani Nyoni
#Date: 03/03/2014
#A program used to check the validity of the time entered by the user.

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

#if (0<=hours<24):
if (hours<0 or hours>23):
    print("Your time is invalid.")
elif (minutes<0 or minutes>59):
    print("Your time is invalid.")
elif (seconds<0 or seconds>59):
    print("Your time is invalid.")
else:
    print("Your time is valid.")