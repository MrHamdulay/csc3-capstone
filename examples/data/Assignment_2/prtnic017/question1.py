# Student Number: PRTNIC017
# Date: 3/7/14

year = eval(input('Enter a year:\n'))

if year % 400 == 0:  # a
    print(year, 'is a leap year.')
elif year % 4 == 0 and year % 100 != 0:
    print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.')