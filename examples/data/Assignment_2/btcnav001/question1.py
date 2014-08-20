x=eval(input("Enter a year:\n"))
def leapyear(x):
    y=x%400
    z=x%4
    a=x%100
    if z==0 and a>0:
        print(x,"is a leap year.")
    elif y==0:
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")

leapyear(x)