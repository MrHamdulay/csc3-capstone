#Author:Thabiso Beau   
#question2.py
k=eval(input("Enter the hours:\n"))
t=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))
if 0 <= k <= 23 and 0 <= t <= 59 and 0 <= z <= 59:
    print("Your time is valid. ") 
else:
    print("Your time is invalid. ") 

