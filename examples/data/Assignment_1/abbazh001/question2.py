# Name: Azhar Aboobaker
# Student Number: ABBAZH001
# Date: 28 February 2014

hours=eval(input("Enter the hours:\n"))

minutes=eval(input("Enter the minutes:\n"))

seconds=eval(input("Enter the seconds:\n"))


if hours>23 or minutes>59 or seconds>59 or hours<0 or minutes<0 or seconds<0:
    print("Your time is invalid.")
else: 
    print("Your time is valid.")


        

      