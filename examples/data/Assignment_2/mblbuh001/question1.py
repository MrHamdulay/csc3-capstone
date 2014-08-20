# Program to determine whether a year is a leap year or not.
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 08 March 2014

x = eval(input("Enter a year:\n"))

if(x%400==0) or (x%4==0) and (x%100!=0):
    print(x,"is a leap year.")
else:
    print(x, "is not a leap year.")