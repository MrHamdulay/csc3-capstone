year= eval(input("Enter a year:\n"))
remainder=year%400
x=year%4
y=year%100
if remainder==0:
    print(year,"is a leap year.")
elif x==0 and y!=0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")