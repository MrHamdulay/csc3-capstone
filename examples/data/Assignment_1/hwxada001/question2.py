#Assignment 1: Question 2:
#Author: Adam Howa
#date 06/03/2014
hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input ("Enter the seconds:\n"))
valid = "valid"
if (hours<0 or hours >23):
   valid = "invalid"
if (minutes<0 or minutes > 59):
   valid = "invalid"
if (seconds<0 or seconds>59):
   valid = "invalid"
print("Your time is",valid,end = '.')