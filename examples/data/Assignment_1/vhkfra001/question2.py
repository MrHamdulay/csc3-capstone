# First define hour, minute and second
# Must be int(input because just input returns a string

hour = int(input ("Enter the hours:\n"))
minute = int(input ("Enter the minutes:\n"))
second = int(input ("Enter the seconds:\n"))


if (0 <= hour <= 23 and 0 <= minute <= 59 
    and 0 <= second <= 59):
    print ("Your time is valid.")
    
else: 
    print ("Your time is invalid.")
    

