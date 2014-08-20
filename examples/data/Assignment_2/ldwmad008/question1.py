y=eval(input('Enter a year:\n'))
x=y%4
if x==0:
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")