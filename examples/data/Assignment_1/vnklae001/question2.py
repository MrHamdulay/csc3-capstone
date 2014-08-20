# A program to test the validity of a time entered by the user
# By: Laene van Niekerk

hours = eval(input("Enter the hours:\n"))   # Gets hour input from user
minutes = eval(input("Enter the minutes:\n"))   # Gets minute input from user
seconds = eval(input("Enter the seconds:\n"))   # Gets second input from user

if 0 <= hours <=23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid.")    # Conditions if the input is valid
else:
    print("Your time is invalid.")  # Conditions if the input is invalid
    
    