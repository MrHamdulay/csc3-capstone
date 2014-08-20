# program to check validity of time
# nokwazi shezi
# 25 february 2014
hours = 0
print ("Enter the hours:")
hours = eval(input())
minutes = 0
(print("Enter the minutes:"))
minutes = eval(input())
seconds = 0
seconds = eval(input ("Enter the seconds: \n"))
#seconds = eval(input())

if hours <= 23 and hours >= 0 :
    if minutes <= 59 and minutes >= 0 :
        if seconds <= 59 and seconds >= 0 :
            print ("Your time is valid.")
        else: print("Your time is invalid.")      
    else: print ("Your time is invalid.")
else :
    print("Your time is invalid.")
    
    