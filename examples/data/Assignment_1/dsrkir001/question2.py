hour = int(input("Enter the hours:\n"))
minute = int(input("Enter the minutes:\n"))
second = int(input("Enter the seconds:\n"))
if (hour<=23 and hour>=0)and (minute<=59 and minute>=0) and (second<=59 and second>=0):
    print("Your time is valid.")
else:
    print("Your time is invalid.")   