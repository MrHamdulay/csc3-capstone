#Determine whether given year is leap or not.
#KVRSHA004

year = eval(input("Enter a year: \n"))

a = year%400
b1 = year%4
b2 = year%100

if (a == 0) or (b1 == 0 and b2 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")