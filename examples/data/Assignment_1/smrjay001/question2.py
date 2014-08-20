#Assignment 1 - Question 2
#Jayan Smart
#26 February 2014

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
if 0<= hours <=23 and 0<= minutes <= 59 and 0<= seconds <= 59: #check the parameters for valid time
    print ("Your time is valid.")
    
else:
    print ("Your time is invalid.")

