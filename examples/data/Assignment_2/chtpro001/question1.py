year=eval(input("Enter a year:\n"))
a=year%400
b=year%4
c=year%100
if (a==0)or(b==0) and (c!=0) :
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
    
        