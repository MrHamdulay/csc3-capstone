#ASSINGMENT 1
#QUESTION 2
#WHTBAS001
#BASIL T WHITEHEAD

import math

def validity():
    
    hours = eval(input("Enter the hours: "))
    print()
    minutes = eval(input("Enter the minutes: "))
    print()
    seconds = eval(input("Enter the seconds: "))
    print()
    
    if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
        print("Your time is valid.")
    else: 
        print("Your time is invalid.")
        
validity()