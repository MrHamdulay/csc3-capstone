hours= eval(input("Enter the hours:\n"))
minutes= eval(input("Enter the minutes:\n"))
seconds= eval(input("Enter the seconds:\n"))
if 0<=hours<24 and 0<=minutes<60 and 0<=seconds<60:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
