x=input('Enter the hours:\n')
y=input('Enter the minutes:\n')
z=input('Enter the seconds:\n')
if 0 <= int(x) <= 23 and 0 <= int(y) <= 59 and 0 <= int(z) <= 59:
    print('Your time is valid.')
else:
    print('Your time is invalid.')