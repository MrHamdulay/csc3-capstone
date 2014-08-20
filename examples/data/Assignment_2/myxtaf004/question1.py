#Author: Moyo, Tafadzwa
#Student Number: MYXTAF004

x=eval(input("Enter a year:\n"))
def leap(x):
    print(x, "is a leap year.")
def notleap(x):
    print(x, "is not a leap year.")
if (x%4==0):
    if(x%100==0):
        if(x%400==0):
            leap(x)
        else: notleap(x)
    else: leap(x)
else: notleap(x)