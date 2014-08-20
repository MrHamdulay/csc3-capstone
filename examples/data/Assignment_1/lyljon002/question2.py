# Question 2, Assignment 0
# Jonathan Leyland, LYLJON002
# 01 March 2014

Hours = eval(input("Enter the hours:\n"))
Minutes = eval(input("Enter the minutes:\n"))
Seconds = eval(input("Enter the seconds:\n"))

Valid = True

if Hours > 23 or Hours < 0:
    Valid = False

if Minutes > 59 or Minutes < 0:
    Valid = False
    
if Seconds > 59 or Seconds < 0:
    Valid = False
    
if Valid == True:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
