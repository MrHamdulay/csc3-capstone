hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if 24<=hours or hours<0 or 60<=minutes or minutes<0 or 60<=seconds or seconds<0: 
 print("Your time is invalid.")
else: print("Your time is valid.")