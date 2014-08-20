#Program to determine whather a year is a leap year or not
#SRXLUC001
#Lucy Sure
#Assignment 2 question 1

year=eval(input("Enter a year:\n"))
answer=year/400 or year/4 or year/100
if(year%400==0 or year%4==0 and year&100!=0):
   print(year,"is a leap year.")
else:
   print(year,"is not a leap year.")
