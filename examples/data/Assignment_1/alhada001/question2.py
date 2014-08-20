hours = 0
minutes = 0
seconds =0
counter = 0
hours = eval(input("Enter the hours: \n"))
minutes = eval(input("Enter the minutes: \n"))
seconds = eval(input("Enter the seconds: \n"))
if hours > 23 or hours <0:
        counter = counter +1 

if minutes > 59 or minutes < 0:
        counter = counter  +1

if seconds > 59 or seconds < 0:
        counter = counter + 1

if counter == 0:
        print("Your time is valid.")
        
if counter > 0: 
        print("Your time is invalid.")
       