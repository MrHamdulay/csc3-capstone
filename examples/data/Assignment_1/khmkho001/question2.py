
s=eval(input("Enter the hours:\n"))
u=eval(input("Enter the minutes:\n"))
v=eval(input("Enter the seconds:\n"))
if(0<=s<=23):
        if(0<=u<=60):
                if(0<=v<=60):
                        print("Your time is valid.")        
                else: 
                        print("Your time is invalid.")
        else: 
                print("Your time is invalid.")
else: 
        print("Your time is invalid.")
    
