# question2.py
# A program that checks the validity of a time entered by the user
# Name: Martin Batek
# Student Number: BTKMAR001
# Date: 25 February 2014

h = eval(input("Enter the hours:\n"))
m = eval(input("Enter the minutes:\n"))
s = eval(input("Enter the seconds:\n"))

if(0<=h<=23) and (0<=m<=60) and (0<=s<=60): # must use "and" when testing for more than one outcome, not ","
    print("Your time is valid.")
else:
    print("Your time is invalid.")
    
