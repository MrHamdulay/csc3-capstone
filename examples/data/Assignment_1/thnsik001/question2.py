#THNSIK001
#ASSIGNMENT 1
#07/03/2014

def times():
    hours = eval(input("Enter the hours: \n"))
    minutes = eval(input("Enter the minutes: \n"))
    seconds = eval(input("Enter the seconds: \n"))
    valid = True
    if( hours < 0 or hours > 23):
        valid = False
    if(minutes <0 or minutes >59):
            valid = False
    if(seconds < 0 or seconds > 59):
                valid =False
    
    if(valid == True):
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
times()
    
    