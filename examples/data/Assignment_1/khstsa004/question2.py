#Validity_of_time.py
h=input("Enter the hours:\n")
m=input("Enter the minutes:\n")
s=input("Enter the seconds:\n")
hours=eval(h)
minutes=eval(m)
seconds=eval(s)
if (0<=hours<=23)and(0<=minutes<=59)and(0<=seconds<=59):
        print("Your time is valid.")
else :
        print("Your time is invalid.")
    

