x = eval(input("Enter a year:\n"))
y = x%400
z = x%4
w = x%100
if y==0:
   print(x,"is a leap year.")
elif z==0 and w!=0:
   print(x,"is a leap year.")
else:
   print(x,"is not a leap year.")