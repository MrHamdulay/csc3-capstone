#A program to determine the validity of the time entered by the user
#Alison Hoernle
#HRNALI002
#27 February 2014

hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if ( hours>=0 and minutes>=0 and seconds>=0 and hours<=23 and minutes<=59 and seconds<=59 ):
        print("Your time is valid.")
else:
        print("Your time is invalid.")


    