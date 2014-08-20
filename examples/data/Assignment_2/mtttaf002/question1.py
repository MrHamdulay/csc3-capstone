#program that determine whether a given year is a leap year or not
#tafara mtutu
#7 mar 2014

year = eval(input("Enter a year:\n"))
#calc = year%400
#calc2 = year%4

if year%100 == 0:
    if year%400 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
elif year%4 == 0:
    print(year, "is a leap year.")
else: print(year, "is not a leap year.")
    
    