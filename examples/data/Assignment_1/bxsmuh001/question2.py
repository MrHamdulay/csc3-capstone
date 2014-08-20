#Assignment 1, Question 2
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 27/02/2014

#Defining a function to check if time is valid.

#Pre-Condition: Input Time in hours, minutes and seconds. Check validity of time.
#Post-Condition: Output validity of time.
def timeValidity():
    
    #Defining Variables
    timeInHours = eval(input("Enter the hours:\n"))
    timeInMinutes = eval(input("Enter the minutes:\n"))
    timeInSeconds = eval(input("Enter the seconds:\n"))
    
    #Checking if time is invalid. Else time is valid.
    if((timeInHours<0 or timeInHours>23) or (timeInMinutes<0 or timeInMinutes>59) or (timeInSeconds<0 or timeInSeconds>59)):
        timeValidity = "Your time is invalid."
    else:
        timeValidity = "Your time is valid."
    
    #Print
    print(timeValidity)

#Output validity test.
timeValidity()
    
    
    