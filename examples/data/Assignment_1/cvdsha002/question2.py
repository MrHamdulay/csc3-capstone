#Shahrain Coovadia
#CVDSHA002
#28/02/2014

hours=eval(input("Enter the hours:"))
print(" ")
minutes=eval(input("Enter the minutes:"))
print(" ")
seconds=eval(input("Enter the seconds:"))
print(" ")

if hours>23 or minutes>59 or seconds>59 or hours<0 or minutes<0 or seconds<0: 
    print("Your time is invalid.")
else: 
    print("Your time is valid.")