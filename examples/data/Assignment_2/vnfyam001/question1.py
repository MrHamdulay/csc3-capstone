x=eval(input("Enter a year:"))

if x%400==0 or x%4==0 and x%100!=0:
   print("\n",x," is a leap year.",sep="")
else:
   print("\n",x," is not a leap year.",sep="")