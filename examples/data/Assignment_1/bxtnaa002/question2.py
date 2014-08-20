# question2.py
# program to check the validity of a time entered by the user as a set of three integers
# author: bxtnaa002

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))
if hours >= 0 and hours <=23:
    if minutes >= 0 and minutes <=59:
        if seconds >= 0 and seconds <=59 : print("Your time is valid.")
        else: print("Your time is invalid.")
    else: print("Your time is invalid.")
else: print("Your time is invalid.")