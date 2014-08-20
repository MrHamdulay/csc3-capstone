hours = eval(input("Enter the hours:\n"))

minutes = eval(input("Enter the minutes:\n"))

seconds = eval(input("Enter the seconds:\n"))

if 23 >= hours and hours >= 0 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
    
    