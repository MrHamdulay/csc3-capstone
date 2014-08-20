# program to check validity of time
# Paul Truter
# 25 February 2014

hours = (0,23)
minutes = (0,59)
seconds = (0,59)

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

if 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
    print("Your time is valid.")
else: print("Your time is invalid.")
