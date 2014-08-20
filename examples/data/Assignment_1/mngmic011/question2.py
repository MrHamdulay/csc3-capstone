#question 2 assignment 1
#Checking time validity entered by user
#Micaela Menegaldo

hours=input("Enter the hours:" "\n")
minutes=input("Enter the minutes:" "\n")
seconds=input("Enter the seconds:" "\n")
hours=eval(hours)
minutes=eval(minutes)
seconds=eval(seconds)
if 0<=hours<=24 and 0<=minutes<60 and 0<=seconds<60:
    print("Your time is valid.")
else:
    print("Your time is invalid.")