year = eval(input('Enter a year:\n'))
#A year is a leap year if (a) it is divisible by 400 or (b) it is divisible by 4 but not by 100.
if ((year%400==0) or ((year%4==0) and (year%100!=0))):
    print(str(year)+' is a leap year.')
else:
    print(str(year)+' is not a leap year.')