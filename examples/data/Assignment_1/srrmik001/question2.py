# Mikhaila Sorour
# 3 March 2014
# Program to check the validity of time

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

if (0 <= hours <= 24) and (0 <= minutes <= 59) and (0 <= seconds <= 59):
    print("Your time is valid.")
else:
    print ("Your time is invalid.")
