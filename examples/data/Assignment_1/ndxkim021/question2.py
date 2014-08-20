hour = eval(input("Enter the hours: \n"))
minute = eval(input("Enter the minutes: \n"))
second = eval(input("Enter the seconds: \n"))


if hour not in range (0,24) or minute not in range (0,60) or second not in range (0,60):
    print("Your time is invalid.")
    
else:
    print("Your time is valid.")
    
