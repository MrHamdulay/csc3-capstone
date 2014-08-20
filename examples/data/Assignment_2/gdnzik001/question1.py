#Author: Godana Zikho
#11 March 2014
#program to determine whether a year is a leap year or not.
year = eval(input("Enter a year:\n"))
if year%400 == 0:   #if year is divisible by 400
    print(year,"is a leap year.")
elif year%4 == 0 and year%100 != 0: #if year is divisible by 4 and not by 100.
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")