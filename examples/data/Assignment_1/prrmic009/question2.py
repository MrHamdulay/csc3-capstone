# program to check the validity of a time entered by user
# Mick Perring
# 27 February 2014

hours = eval(input("Enter the hours: ""\n")) 
# allows user to enter hours

minutes = eval(input("Enter the minutes: ""\n")) 
# allows user to enter minutes

seconds = eval(input("Enter the seconds: ""\n")) 
# allows user to enter seconds

if hours < 0:
    print ("Your time is invalid.")
elif hours > 23:
    print ("Your time is invalid.")
    # checks validity of hours entered
    
elif minutes < 0:
    print ("Your time is invalid.")
elif minutes > 59:
    print ("Your time is invalid.")
    # checks validity of minutes entered
    
elif seconds < 0:
    print ("Your time is invalid.")
elif seconds > 59:
    print ("Your time is invalid.")
    # checks validity of seconds entered
    
else:
    print ("Your time is valid.")
    # informs user if time is valid