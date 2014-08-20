#Zikho Godana GDNZIK001
#4 march 2014
#program to check the validity of a time entered by a user as a set of three integers
hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

if (hours<0) or (hours>24) or (minutes<0) or (minutes>60) or (seconds<0) or (seconds>60):
    print("Your time is invalid.")
else:
    print("Your time is valid.")