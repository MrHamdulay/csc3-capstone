Hours=eval(input("Enter the hours:\n",))
Minutes=eval(input("Enter the minutes:\n"))
Seconds=eval(input("Enter the seconds:\n"))
if Hours in range(0,24) and Minutes in range(0,60) and Seconds in range(0,60):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
