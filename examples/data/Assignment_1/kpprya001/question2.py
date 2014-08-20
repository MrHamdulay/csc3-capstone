#Ryan Kopping
#Question 2 
#KPPRYA001

hour = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
 

if hour >= 0 and hour <= 23:
    if minutes >= 0 and minutes <= 59:
        if seconds >=0 and seconds <= 59:
            print ("Your time is valid.")
        else:
            print ("Your time is invalid.")
    else:
        print("Your time is invalid.")
            
else:
    print ("Your time is invalid.")

            