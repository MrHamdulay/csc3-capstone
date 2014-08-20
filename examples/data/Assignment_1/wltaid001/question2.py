#Aiden Walton
#WLTAID001
#Program to check the validity of a time entered by the user as a set of three integers

hours=0 #Variable to store hours
minutes=0 #Variable to store minutes
seconds=-0 #variable to store seconds

hours=eval(input("Enter the hours:\n")) #ask user for hours variable
minutes=eval(input("Enter the minutes:\n")) #ask user for muinutes variable
seconds=eval(input("Enter the seconds:\n")) #ask user for seconds variable

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59: #evaluate time input
    print("Your time is valid.")

else:
    print("Your time is invalid.") #Print message if time is invalid
