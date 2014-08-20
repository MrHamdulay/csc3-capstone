# Name: Hamza Ebrahim           06/03/14
# Assignment 1 CSC1015F 
# Question 2



hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

if (hours > 23) or (hours < 0) or (minutes > 59) or (minutes < 0) or (seconds > 59) or (seconds < 0): 
    print("Your time is invalid.")

else: print("Your time is valid.")

