#Program to determine whether a year is a leap year or not
#Nikhil Jiten Naik (NKXNIK003)
#8th of March 2014

year = eval(input("Enter a year:\n"))

if year%400 ==0 or year%4 ==0:
    print(year,"is a leap year.")
    
else:
    print(year,"is not a leap year.")
