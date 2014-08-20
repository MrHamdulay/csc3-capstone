hours,minutes,seconds=eval(input("Enter the hours:\n")),eval(input("Enter the minutes:\n")),eval(input("Enter the seconds:\n"))
valid =False
if(hours>=0 and hours<=23 and minutes>=0 and minutes<=59 and seconds>=0 and seconds<=59):
        valid=True
        
if(valid==True):
        print("Your time is valid.")
else:
        print("Your time is invalid.")
