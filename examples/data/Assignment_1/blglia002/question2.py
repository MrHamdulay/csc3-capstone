#Liam Blignaut
#Program to check the validity of time
#28/02/14

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
if (hours<0) or (hours>23) or (minutes<0) or (minutes>59) or (seconds<0) or (seconds>59):
    print("Your time is invalid.")
else:
    print("Your time is valid.")