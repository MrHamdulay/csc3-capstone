hours= input("Enter the hours:""\n")
minutes= input("Enter the minutes:""\n")
seconds= input("Enter the seconds:""\n")

hours=eval(hours)
minutes=eval(minutes)
seconds=eval(seconds)
def time(hours, mintes, seconds):
    if (hours>23) or (minutes>59) or (seconds>59):
        print("Your time is invalid.")
    elif(hours<0) or (minutes<0) or (seconds<0):
        print("Your time is invalid.")
    else:
        print("Your time is valid.")
        
   
        
time(hours, minutes, seconds)
