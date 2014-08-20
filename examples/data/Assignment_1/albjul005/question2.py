# Program to check the validity of time in a specified range
# Julian Albert
# 27 February 2014

# allows hours input integers only
hours = eval(input("Enter the hours: " '\n' )) 

# allows minutes input integers only
minutes = eval(input("Enter the minutes: " '\n'))

# allows seconds input integers only
seconds = eval(input("Enter the seconds: " '\n'))

# check if hours, minutes, seconds falls within the required range
if (hours <= 23 and hours >= 0 and minutes <= 59 and minutes >= 0 and seconds >= 0 and seconds <= 59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
    
    

    



   


    
    