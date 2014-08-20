# Program to check validity of time entered by the user
# Shivam Ragoonaden
# 26 February 2014

Hours = eval(input("Enter the hours:\n"))
Minutes = eval(input("Enter the minutes:\n"))
Seconds = eval(input("Enter the seconds:\n"))

Valid = True

if Hours < 0 or Hours > 23:
    Valid = False
if Minutes < 0 or Minutes > 59:
    Valid = False
if Seconds < 0 or Seconds > 59:
    Valid = False
    
if Valid == False:
    print("Your time is invalid.")
else:
    print("Your time is valid.")
    
    