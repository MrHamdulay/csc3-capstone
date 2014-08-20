# Checking if the time entered is valid
# Thiloshni Moodley
# MDLTHI019

import math

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

# Check whether the time entered is valid

if hours >24 or hours <0 or minutes >59 or minutes <0 or seconds >59 or seconds <0:
    print("Your time is invalid.")
else: print("Your time is valid.")

    
 
    
