H= eval(input("Enter the hours:\n"))
M= eval(input("Enter the minutes:\n"))
S= eval(input("Enter the seconds:\n"))

if (0<=H<=23) and (0<=M<=59) and (0<=S<=59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")

