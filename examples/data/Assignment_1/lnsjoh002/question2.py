#program to check whether a time is valid 
#JP Lanser
#25 feb 2014

def time():
    hours=eval(input("Enter the hours:\n" )) 
    minutes=eval(input("Enter the minutes:\n")) 
    seconds=eval(input("Enter the seconds:\n")) 
    if hours>=0 and minutes>=0 and seconds>=0 and hours<=23 and minutes<=59 and seconds<=59 and type(hours)==int and type(minutes)==int and type(seconds)==int:
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
    
time()
        


    
    
