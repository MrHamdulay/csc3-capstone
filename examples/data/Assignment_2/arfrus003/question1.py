#Rushka Ariefdien
#assignment 2
#question 1
year = eval(input("Enter a year: \n"))
import math
if year%100!=0 and year%4==0 or year%400==0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

