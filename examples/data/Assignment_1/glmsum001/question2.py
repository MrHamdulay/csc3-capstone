#Name: Sumayah Goolam Rassool
#Student Number:GLMSUM001
#Date : 01 March 2014
#Assignment 1

import math

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
 
if(hours<0 or hours>24):
    print("Your time is invalid.")
    
elif(minutes<0 or minutes>59):
    print("Your time is invalid.")
        
elif(seconds<0 or seconds>59):
    print("Your time is invalid.")
else:
    print("Your time is valid.")
 