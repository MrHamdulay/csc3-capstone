hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
if not (0<=hours<=23):
    print("Your time is invalid.")
elif not (0<=minutes<=59):
    print("Your time is invalid.")
elif not (0<=seconds<=59):
    print("Your time is invalid.")
else:
    print("Your time is valid.")