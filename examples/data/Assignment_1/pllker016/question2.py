h=input("Enter the hours:\n")
h=eval(h)
m=input("Enter the minutes:\n")
m=eval(m)
s=input("Enter the seconds:\n")
s=eval(s)
if(0<=h<=23)and(0<=m<=59)and(0<=s<=59):
 print("Your time is valid.")
else:
 print("Your time is invalid.")