#KRWANE001

yr=eval(input("Enter a year:\n"))
x=int(yr%4) 
y=int(yr%400)
z=int(yr%100>0)

if y==0 or x==0 and z :
    print(yr,"is a leap year.")
else :
    print(yr, "is not a leap year.")