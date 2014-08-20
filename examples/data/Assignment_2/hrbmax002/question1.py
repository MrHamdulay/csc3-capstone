year = eval(input("Enter a year:\n"))

is_leap_400 = year%400
is_leap_100 = year%100
is_leap_4 = year%4

if is_leap_400 == 0 or is_leap_100 != 0 and is_leap_4 == 0:
    print (year, "is a leap year.")
else:
    print (year, "is not a leap year.")
