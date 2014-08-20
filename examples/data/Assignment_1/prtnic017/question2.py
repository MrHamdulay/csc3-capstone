# Assignment 1 - Question 2
# Student Number: PRTNIC017
# 25 - 2 - 2014

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

if 23 >= hours >= 0:
    if 59 >= minutes >= 0:
        if 59 >= seconds >= 0:
            print("Your time is valid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
else:
    print("Your time is invalid.")