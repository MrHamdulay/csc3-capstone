# A progaramme designed to calculate if a year is a leap year or not
# Created by: Jenna Lake
# Date: 7/3/2014

num=eval(input("Enter a year: \n"))
if num%400==0:
    print(num, "is a leap year.")
elif num%400>0:
    if num%100==0:
        print(num, "is not a leap year.")
    elif num%100>0:
        remainder=num%4
        if remainder>0:
            print(num, "is not a leap year.")
        elif remainder==0:
            print(num, "is a leap year.")