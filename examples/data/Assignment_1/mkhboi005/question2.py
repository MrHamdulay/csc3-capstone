hours=eval(input('Enter the hours: \n'))
Minutes=eval(input('Enter the minutes: \n'))
seconds=eval(input('Enter the seconds: \n'))

if (Minutes > 59) or (Minutes < 0) or (hours > 23) or (hours < 0) or (seconds > 59) or (seconds < 0):
    print('Your time is invalid.')
else:
    print('Your time is valid.')