#KRTDAK001h
hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
def time():
    if (hours <= 24) and (hours >= 0):
        if (minutes <= 60) and (minutes >= 0):        
            if (seconds <= 60) and (seconds >= 0):
                print("Your time is valid.")
            else:
                print("Your time is invalid.")
        else:
            print("Your time is invalid.")        
    else:
        print("Your time is invalid.")
        
time()