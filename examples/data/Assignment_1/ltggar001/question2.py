Hours = eval(input("Enter the hours:\n"))
Minutes = eval(input("Enter the minutes:\n"))
Seconds = eval(input("Enter the seconds:\n"))
if 0<=Hours<=23 and 0<=Minutes<=59 and 0<=Seconds<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")