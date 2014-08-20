x=eval(input("Enter a year:\n"))
y= x%4
z= x%400
w= x%100
if z==0 or w!=0 and y==0:
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")