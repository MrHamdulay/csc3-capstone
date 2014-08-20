hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

invalid = 0

if hours < 0 or hours > 23:
    invalid = 1

if minutes < 0 or minutes > 59:
    invalid = 1

if seconds < 0 or seconds > 59:
    invalid = 1
    
if invalid:
    print("Your time is invalid.")
else:
    print("Your time is valid.")
