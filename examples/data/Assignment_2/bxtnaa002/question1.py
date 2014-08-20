# question1.py
# a program to determine whether a year is a leap year or not.
# author: bxtnaa002

year = eval(input("Enter a year:\n"))
if (year % 400) == 0:
    print (year, "is a leap year.")
elif (year% 100) == 0:
    print (year, "is not a leap year.")
elif ( year % 4) == 0:
    print (year, "is a leap year.")
else: 
    print (year, "is not a leap year.")