#program to check validity of entered time
#Robin Hall
#25/02/2014

def timevalid():
    hour=eval(input("Enter the hours:\n"))
    minute=eval(input("Enter the minutes:\n"))
    second=eval(input("Enter the seconds:\n"))
    
    if hour >=0 and hour <=23 and minute >=0 and minute <=59 and second >=0 and second <=59:
        print("Your time is valid.")
    
    else:
        print("Your time is invalid.")

timevalid()
    

