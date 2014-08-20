#program to check validity of time
x= eval(input("Enter the hours:" "\n"))
y= eval(input("Enter the minutes:" "\n"))
z= eval(input("Enter the seconds:" "\n"))
if 0<=x<=23:
 if 0<=y<=59:
  if 0<=z<=59:
   print("Your time is valid.")
  else:
    print("Your time is invalid.") 
 else:
     print("Your time is invalid.") 
else:
 print("Your time is invalid.")
 

  
 

