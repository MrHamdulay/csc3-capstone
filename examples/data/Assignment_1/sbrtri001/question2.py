# Assignment 1, question 2
# Tristan Subroyen, SBRTRI001

hours = eval(input("Enter the hours: \n",))
if 0<= hours <= 23:
    hoursCheck = 0
else: hoursCheck = 1

minutes = eval(input("Enter the minutes: \n"))
if 0<= minutes <= 59:
    minutesCheck = 0
else: minutesCheck = 1

seconds = eval(input("Enter the seconds: \n"))
if 0<= seconds <= 59:
    secondsCheck = 0
else: secondsCheck = 1

timeCheck = hoursCheck + minutesCheck + secondsCheck
if timeCheck == 0:
    print("Your time is valid.")
else: print("Your time is invalid.")