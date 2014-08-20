# Program to check validity of input of time
# Nevarr Pillay
# 25 February 2014

try:
    hrs = eval(input("Enter the hours: \n"))
    mins = eval(input("Enter the minutes: \n"))
    secs = eval(input("Enter the seconds: \n"))   
    
    if(type(hrs) == int and type(mins) == int and type(secs) == int):
        if(hrs < 0 or hrs > 23 or mins < 0 or mins > 59 or secs < 0 or secs > 59):
            print("Your time is invalid.")
        
        else:
            print("Your time is valid.")
            
    else:
        print("Your time is invalid.")    
except NameError:
    print("Your time is invalid.")
    

