#Program to check validity of time 


time1=eval(input("Enter the hours:\n"))

time2=eval(input("Enter the minutes:\n"))

time3=eval(input("Enter the seconds:\n"))

if 0<=time1<=23 and 0<=time2<=59 and 0<=time3<=59: 
    print("Your time is valid.")
else: 
    print("Your time is invalid.")
    

    

