#Question 2: Assignment 1
#Tashfia Amin
#AMNTAS003

def time():
    x=eval(input("Enter the hours: \n"))
    y=eval(input("Enter the minutes: \n"))
    z=eval(input("Enter the seconds: \n"))
    
    if x<0 or x>23 or y<0 or y>59 or z<0 or z>59:
        print("Your time is invalid.")
    else:
        print("Your time is valid.")

time()
