# Program to deterime a gap year
# Kristin Kinmont
# 8 march 2014

year=eval(input("Enter a year:\n"))
if year%400==0: # check if year is divisible by 400
    print(year,"is a leap year.")
elif year%4==0 and year%100>0: # check if year is divisible by 4 but not by 100
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
    
