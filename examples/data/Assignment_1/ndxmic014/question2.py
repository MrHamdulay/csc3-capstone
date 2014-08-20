#NDXMIC014
#Question2

print('Enter the hours:')
hour = eval(input())
print('Enter the minutes:')
Min = eval(input())
print('Enter the seconds:')
sec = eval(input())
if ((0<= hour <= 23) and (0 <= Min <= 59) and (0<= sec <= 59)):
    print('Your time is valid.')
else:
    print('Your time is invalid.')
