#Student number: MKHBOI005
#Name: Tumi
#Determine whether the year is a leap year or not
#Date: 13 March 2014

def isit():
    import math
    k=eval(input("Enter a year:\n"))
    p=k%400
    n=k%4
    a=k%100
    if (p==0) or (n==0) and (a!=0):
        print(k,"is a leap year.")
    else:
        print(k,"is not a leap year.")

isit()