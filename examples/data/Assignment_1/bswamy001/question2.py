#Amy Bosworth
#Program to check Validity of time
#Assignment 1, question 2


hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

def time():
    if (hours<0) or (hours>23):
        print("Your time is invalid.")
    elif (minutes<0) or (minutes>59):
        print("Your time is invalid.")
    elif (seconds<0) or (seconds>59):
        print("Your time is invalid.")
    else: 
        print("Your time is valid.")
        
time()
    



   



    


