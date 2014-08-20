#student number:DNLAAR001
#Name:Aaron Daniels
x=eval(input('Enter the hours:\n'))
y=eval(input('Enter the minutes:\n'))
z=eval(input('Enter the seconds:\n'))
if (0 <= x < 24) and (0 <= y < 60) and (0 <= z < 60):
    print('Your time is valid.')
else:
    print('Your time is invalid.')
 