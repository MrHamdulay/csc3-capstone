a=eval(input("Enter the hours:\n"))
b=eval(input("Enter the minutes:\n"))
c=eval(input("Enter the seconds:\n"))

if(a>=0 and a<=23 and b>=0 and b<=59 and c>=0 and c<=59):
   print("Your time is valid.")

else:
   print("Your time is invalid.")