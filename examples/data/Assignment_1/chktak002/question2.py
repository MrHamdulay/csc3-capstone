hours =eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n")) 
seconds=eval(input("Enter the seconds:\n"))
Valid = True
if (hours<0) or (hours>23):
    Valid= False            
if(minutes<0) or (minutes>59):
    Valid= False                        
if(seconds<0) or (seconds>59):
    Valid=False     

if Valid == False: 
    print("Your time is invalid.")
else:
    print("Your time is valid.")
