# tlholo lichaba
# program to determine validity of time

hours = eval(input("Enter the hours:"+'\n'))
minutes = eval(input("Enter the minutes:"+'\n'))
seconds = eval(input("Enter the seconds:"+'\n'))

if (hours<0 or hours>23):
    print("Invalid time")
elif (minutes<0 or minutes>59):
    print("Invalid time")
elif (seconds<0 or seconds>59):
    print("Invalid time")
else:
    print("The time is valid")