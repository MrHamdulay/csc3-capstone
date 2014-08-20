year=eval(input('Enter a year:\n'))
if year/400==year//400 or year/4==year//4 and year/100!=year//100:
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')