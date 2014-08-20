#Time check program
# Question2.py
# Author: Litha Maqungo
# 2 March 2014

print("Enter the hours:")
hours=eval(input())
print("Enter the minutes:")
minutes=eval(input())
print("Enter the seconds:")
seconds=eval(input())

if (hours<0) or (hours>24) :
    print("Your time is invalid.")
else:
    if (minutes<0) or (minutes>60) :
        print("Your time is invalid.")
    else:
        if (seconds<0) or (seconds>60) :
            print("Your time is invalid.")
        else:
            print("Your time is valid.")



