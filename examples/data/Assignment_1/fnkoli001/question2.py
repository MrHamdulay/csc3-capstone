hour=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

if (type(hour) == int and hour>=0 and hour<=23) and (type(minutes) == int and minutes>=0 and minutes<=59) and (type(seconds) == int and seconds>=0 and seconds<=59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")