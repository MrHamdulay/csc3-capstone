#Leap year
year = eval(input("Enter a year:\n"))
leap_year = 0

if year%400 == 0:
    leap_year = 1
    
elif year%4 == 0 and year%100 != 0:
    leap_year = 1
    
if leap_year == 1:
    print(year,"is a leap year.\n")
    
else:
    print(year,"is not a leap year.")
    