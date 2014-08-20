#Assignment 1
#Question 2
#Daniel Schwartz
#SCHDAN037
#25/02/2014

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

valid = False

if(hours >= 0 and hours <= 23):
    if(minutes >= 0 and minutes <= 59):
        if(seconds >= 0 and seconds <= 59):
            valid = True

if(valid):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
