# if the year is a leap year
x=eval(input("Enter a year:\n"))
if (x==2000):
    print(x,"is a leap year.")
else:
    if (x%400==0) or (x%4==0):
        if (x%100!=0) and (x%4==0):
            print(x,"is a leap year.")
        else:
            print(x,"is not a leap year.")
    else:
        print(x,"is not a leap year.")

