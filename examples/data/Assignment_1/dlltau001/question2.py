#Author - Tauriq Dolley
#Question 2 / Assignment 1

validity = "valid." #declare as valid initially until proven otherwise

hours = eval( input("Enter the hours: \n")) #user inputs hours value

if (hours > 23 or hours < 0):
    
        validity = "invalid."
   
minutes = eval( input("Enter the minutes: \n")) #user inputs minutes value

if (minutes < 0 or minutes > 59):
        
        validity = "invalid."
    
seconds = eval( input("Enter the seconds: \n")) #user inputs seconds value

if (seconds < 0 or seconds > 59):
                
        validity = "invalid."
            
            
print("Your time is "+validity)