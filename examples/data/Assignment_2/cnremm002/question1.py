n=input("Enter a year:\n")
n = int(n)
if n%400==0 or n%4==0 and n%100!=0:
   print (str(n),"is a leap year.")
else:
   print (str(n),"is not a leap year.")