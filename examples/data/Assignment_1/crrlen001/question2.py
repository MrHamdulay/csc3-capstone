Hour = eval(input("Enter the hours:\n") )
Minute = eval(input("Enter the minutes:\n") )
Second = eval(input("Enter the seconds:\n") )

if (Hour>=0) and (Hour<=23) and (Minute>=0) and (Minute<=59) and (Second>=0) and (Second<=59):
    print("Your time is valid.")
elif Hour < 0:
    print("Your time is invalid.")
elif Hour > 23:
    print("Your time is invalid.")
elif Minute < 0:
    print("Your time is invalid.")
elif Minute > 59:
    print("Your time is invalid.")
elif Second < 0:
    print("Your time is invalid.")
elif Second > 59:
    print("Your time is invalid.")
        
#Author: Lenard Carroll
#Student_Number: CRRLEN001        
