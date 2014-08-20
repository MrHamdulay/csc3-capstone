#Question 2
#Program to check the validity of a time entered by a user
import math
Hours=eval(input("Enter the hours:\n"))
Minutes=eval(input("Enter the minutes:\n"))
Seconds=eval(input("Enter the seconds:\n"))
if 0<=Hours<=23 and 0<=Minutes<60 and 0<=Seconds<60:
    print("Your time is valid.")
else: 
    print("Your time is invalid.")