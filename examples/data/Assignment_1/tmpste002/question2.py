# TMPSTE002 - Stephen Temple

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
second_s = eval(input("Enter the seconds:\n"))
if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and second_s >= 0 and second_s <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")