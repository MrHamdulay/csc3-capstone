year = eval(input("Enter a year:\n"))
x=year%400
y=year%4
z=year%100
if x==0:
    print(year,"is a leap year.")
elif y==0 and z!=0 :
    print(year,"is a leap year.")
else :
    print(year,"is not a leap year.")