#Time Validity Check
#Assignment 1, Question 2
#By Tejasvin Bagirathi BGRTEJ001

hours = eval(input("Enter the hours:\n"))
mins = eval(input("Enter the minutes:\n"))
secs = eval(input("Enter the seconds:\n"))

if (0 <= hours < 24) and (0 <= mins <=60 ) and (0 <= secs <= 60):
    print ("Your time is valid.")
else: print("Your time is invalid.")
    
        
        
