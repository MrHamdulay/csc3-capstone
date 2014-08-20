hours = eval(input ("Enter the hours:"))
print("")
minutes = eval(input ("Enter the minutes:"))
print("")
seconds = eval(input ("Enter the seconds:"))
print("")
valid = 0
if (hours > -1 and hours < 24):
    hours = 0
else : valid = 1
        
        
if (minutes > -1 and minutes < 60):
    minutes = 0
else : valid = 1
    
    
    
if (seconds > -1 and seconds < 60):
       seconds = 0
else :  valid = 1    
    
if (valid == 1):
    print("Your time is invalid.")
    
else: print("Your time is valid.")
        
        
    