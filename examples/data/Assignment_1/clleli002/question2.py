#Program to check the validity of a time entered by the user as a set of 3 integers.
#Name: Elizabeth Cilliers
#Student Number: CLLELI002
#Date: 26 February 2014

def time():
        if hours<0 or hours>23:
                print("Your time is invalid.")
        elif minutes<0 or minutes>59:
                print("Your time is invalid.")
        elif seconds<0 or seconds>59:
                print("Your time is invalid.")
        else:
                print("Your time is valid.")

hours= input("Enter the hours:\n")
minutes= input("Enter the minutes:\n")
seconds= input("Enter the seconds:\n")
hours=eval(hours)
minutes=eval(minutes)
seconds=eval(seconds)

time() 

    


