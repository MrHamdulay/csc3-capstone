x=eval(input('Enter the hours:\n'))
y=eval(input('Enter the minutes:\n'))
z=eval(input('Enter the seconds:\n'))
if x>23 or x<0 or y>59 or y<0 or z>59 or z<0:
    print('Your time is invalid.')
else: print('Your time is valid.')