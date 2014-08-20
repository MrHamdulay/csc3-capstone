x= eval(input('Enter a year:'"\n"))
y= x%4
z=x%100
t=x%400





if (t==0) or (y==0 and z!=0):
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")

    