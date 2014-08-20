hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

if hours in range(0,24) and minutes in range(0,60) and seconds in range(0,60): 
    print("Your time is valid.")
else:
    print("Your time is invalid.")