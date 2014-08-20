hours=eval(input('Enter the hours:\n'))
minutes=eval(input('Enter the minutes:\n'))
seconds=eval(input('Enter the seconds:\n'))
if hours>23: 
    print('Your time is invalid.')
elif hours<0:
    print
    print('Your time is invalid.')
elif minutes>59:
    print('Your time is invalid.')
elif minutes<0:
    print('Your time is invalid.')
elif seconds>59:
    print('Your time is invalid.')
elif seconds<0:
    print('Your time is invalid.')
else: 
    print('Your time is valid.')


