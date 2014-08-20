
hour = eval(input('Enter the hours:\n'))
minu = eval(input('Enter the minutes:\n'))
sec = eval(input('Enter the seconds:\n'))

if ((0 <= hour <= 23) and (0<=minu<=59) and  (0<=sec<=59)):
    print('Your time is valid.')
else:
    print('Your time is invalid.')

    
