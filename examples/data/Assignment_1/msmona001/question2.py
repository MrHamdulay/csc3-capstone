#Question 2
#Assignment 1
#Onalerona Mosimege

check = 0
hours = eval(input("Enter the hours:\n"))
if (hours <= 23) and (hours >= 0):
    check = check +1
minutes = eval(input("Enter the minutes:\n"))
if (minutes <= 59 and minutes >=0) :
    check = check +1   
seconds = eval(input("Enter the seconds:\n"))
if (seconds <= 59 and seconds >=0) :
    check = check +1  
    
if check == 3:
    print("Your time is valid.")
else:
    print("Your time is invalid.")