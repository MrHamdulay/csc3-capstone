hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if (hours>23) or (hours<0) or (minutes>60) or (minutes<0) or (seconds>60) or (seconds<0):
    print("Your time is invalid.")
else:
    if(0<=hours<=23) and (0<=minutes<=60) and (0<=seconds<=60):
        print("Your time is valid.")