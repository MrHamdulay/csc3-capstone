
print('Enter the hours:')
h = eval(input())

print('Enter the minutes:')
m = eval(input())

print('Enter the seconds:')
s = eval(input())

if ((h >= 0) and (h <= 23) and (m >= 0) and (m <= 59) and (s >= 0) and (s <= 59)):
    print('Your time is valid.')
else:
    print('Your time is invalid.')
