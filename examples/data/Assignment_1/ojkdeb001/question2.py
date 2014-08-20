hours = int(input("Enter the hours: \n")) 
minutes = int(input("Enter the minutes: \n"))
seconds = int(input("Enter the seconds: \n"))
if ((hours<0) or (hours>23)) or ((minutes<0) or (minutes>59)) or ((seconds<0) or (seconds>59)) :
    print("Your time is invalid.")
else: print("Your time is valid.")