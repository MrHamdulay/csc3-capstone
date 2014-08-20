# program to determine whether a year is a leap year or not
# by: khadeejah omar
# 7 march 2014

year = eval(input("Enter a year:\n"))

if year % 400 == 0 :            # tests if divisible by 400
    print(year, "is a leap year.")
elif year % 4 == 0 and year % 100 > 0 :            # tests if divisible by 4 but not by 100
    print(year, "is a leap year.")
else: print(year, "is not a leap year.")