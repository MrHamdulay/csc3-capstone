
hrs=eval(input("Enter the hours:\n"))
mins=eval(input("Enter the minutes:\n"))
secs=eval(input("Enter the seconds:\n"))

if(0<=hrs<=23):
    
    if(0<=mins<=59):
        
        if(0<=secs<=59):
            print("Your time is valid.")
        else: print("Your time is invalid.")
    else: print("Your time is invalid.")
else: print("Your time is invalid.")