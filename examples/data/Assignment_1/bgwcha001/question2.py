h=eval(input("Enter the hours:\n"))
m=eval(input("Enter the minutes:\n"))
s=eval(input("Enter the seconds:\n"))

x=0

if 0<=h<=23:
 x=x+1
else:
 x=x
 
 
if 0<=m<=59:
 x=x+1
else:
  x=x
  
 
if 0<=s<=59:
 x=x+1
else:
 x=x

if x<3:
 print("Your time is invalid.")
 #print(x)
else:
 print("Your time is valid.")
 #print(x)
 
 
 