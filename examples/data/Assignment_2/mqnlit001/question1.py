#Program to determine a leap year
# Author: Litha Maqungo
# 11 March 2014

print("Enter a year:")
year=eval(input())

if year % 400 == 0:
    print(year,"is a leap year.") 
else:
    if year % 4 == 0 and year % 100 > 0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
    

  