#program to determine if a year is a leap year
# 10 March 2014

year=eval(input("Enter a year: \n"))
year/400
year/100
year/4

if year%400==0 or (year%4==0 and year%100!=0):
    print(year,"is a leap year.")
    
else: print(year,"is not a leap year.")

