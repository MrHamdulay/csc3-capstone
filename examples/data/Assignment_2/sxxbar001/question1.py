# Assignment 2
# Question 1
# Barry Su
# SXXBAR001
# 11 March 2014

year= eval(input("Enter a year:\n"))
if year%400==0 or year%4==0 and year%100!=0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")