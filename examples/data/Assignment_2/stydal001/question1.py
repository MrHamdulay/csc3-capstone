# Dalise Steynfaard
# STYDAL001
# Assignment 2, question 1
# March 2013

year = eval(input("Enter a year:\n"))

if year % 400 == 0 or (year % 4 == 0 and not(year % 100 == 0)):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")