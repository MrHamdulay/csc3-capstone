#Program to test validity of user-input time
#Kavir Ranchod RNCKAV001
#05/03/2014

hrs = eval(input("Enter the hours:\n"))
mins = eval(input("Enter the minutes:\n"))
secs = eval(input("Enter the seconds:\n"))

if (hrs > 23 or hrs < 0 or mins > 59 or mins < 0 or secs > 59 or secs < 0):
   print("Your time is invalid.")

else:
   print("Your time is valid.")