hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

if hours>=0 and hours<=24:
    if minutes>=0 and minutes<60:
        if seconds>=0 and seconds<=60:
            print("Your time is valid.") 
        else:
            print("Your time is invalid.")        
        
    else:
        print("Your time is invalid.")    
else:
    print("Your time is invalid.")
 
