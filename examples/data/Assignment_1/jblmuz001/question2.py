#Question_2

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

test=False

if (hours>=0) and (hours<=23):
                
                if minutes>=0 and minutes<=59:
                                if seconds>=0 and seconds<=59:
                                                test=True                                

 
if(test==True):
                print("Your time is valid.")
else:
                print("Your time is invalid.")
                 
  

    
    


