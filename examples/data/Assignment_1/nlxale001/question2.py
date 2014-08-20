#Author: NLXALE001
#Date: 25 Feb 2014
#Assignment 1
prompt = "Enter the hours: \n"
hours=eval(input(prompt))
prompt = "Enter the minutes: \n"
minutes=eval(input(prompt))
prompt = "Enter the seconds: \n"
seconds=eval(input(prompt))
if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print ("Your time is valid.")
else:
    print ("Your time is invalid.")