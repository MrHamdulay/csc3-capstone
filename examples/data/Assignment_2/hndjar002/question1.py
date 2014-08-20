# Assignment 2
# Jaren Hendricks
# 07 March 2014

# Programme to calculate whether a year is a leap year or not. 

year = eval(input("Enter a year:\n"))

if (year%400== 0) or (year%4==0) and not year%100==0:
    print(year,"is a leap year.")
else:
    print(year, "is not a leap year.")