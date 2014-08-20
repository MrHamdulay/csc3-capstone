
y = int(input('Enter a year:\n'))

if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
    print(y, 'is a leap year.')
else:
    print(y, 'is not a leap year.')

