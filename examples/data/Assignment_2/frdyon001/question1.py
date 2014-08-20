#Student number: FRDYON001
#Name: Yonela Ford
#Programme to determine whether the year is a leap year or not
#Date: 08 March 2014

def leap():
    import math
    x=eval(input("Enter a year:\n"))
    y=x%400
    z=x%4
    a=x%100
    if (y==0) or (z==0) and (a!=0):
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")

leap()