year=int(input("Enter a year:\n"))
a=year%400
b=year%100
c=year%4
if a==0:
    print(year,"is a leap year.")
elif b==0:
    print(year,"is not a leap year.")
elif c==0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
