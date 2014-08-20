#Program to check time is valid
#James Lloyd    
#LLYJAM001
#

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

if hours<0 or hours>23 or minutes<0 or minutes>59 or seconds<0 or seconds>59:
    output="Wrong"
    print("Your time is invalid.")
else:
    output="Right"
    print("Your time is valid.")
