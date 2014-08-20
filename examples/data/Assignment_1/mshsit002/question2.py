hours=eval(input('\nEnter the hours: '))
minutes=eval(input('\nEnter the minutes:'))
seconds=eval(input('\nEnter the seconds:'))
if hours >= 0 and hours<=23 and minutes>=0 and minutes<=59 and seconds>=0 and seconds<=59:
    print('\nYour time is valid.')
else:
    print('\nYour time is invalid.')