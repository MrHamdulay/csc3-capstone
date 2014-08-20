#James Nevin, NVNJAM003
#Question 2, Assignment 1

#Take in user input can confirm whether in range
x = eval(input("Enter the hours:\n")) in range (0, 24)
y = eval(input("Enter the minutes:\n")) in range (0, 60)
z = eval(input("Enter the seconds:\n")) in range (0, 60)

if (x and y and z): #All user inputs valid
    print ("Your time is valid.")
else: #Invalid inputs
    print ("Your time is invalid.")