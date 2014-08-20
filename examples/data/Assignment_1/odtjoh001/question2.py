
hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

def output(hrs, minu, sec):
    if (hrs >= 0 and hrs <= 23):
        if(minu >= 0 and minu <= 59):
            if(sec >= 0 and sec<= 59):
                print("Your time is valid.")
            else:
                    print("Your time is invalid.")                
        else:
            print("Your time is invalid.")                    
    else:
        print("Your time is invalid.")
        
output(hours, minutes, seconds)

    
    
    

