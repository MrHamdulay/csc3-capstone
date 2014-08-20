# Question 2
# Name: Khanyisile Morudu
# Student Number: mrdkha001
# Date: 05/03/2014

hours = eval(input("Enter the hours: \n"))
minutes = eval(input("Enter the minutes: \n"))
seconds = eval(input("Enter the seconds: \n"))
if (hours in range(24)) and (minutes in range(61)) and (seconds in range(61)):
    print("Your time is valid.")
else:
    print("Your time is invalid.")