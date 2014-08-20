#Programme to validate time
#STUDENT NUMBER: DDNAMI001
#Amitha Doodnath
#04 March 2014

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

if(0<=hours<=23):
    
    if(0<=minutes<=59):
        
        if(0<=seconds<=59):
            print("Your time is valid.")
        else: print("Your time is invalid.")
    else: print("Your time is invalid.")
else: print("Your time is invalid.")
    

    

    