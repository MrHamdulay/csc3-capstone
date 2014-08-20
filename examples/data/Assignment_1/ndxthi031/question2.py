#NDXTHI031
#Assignment 1
#Question2

print('Enter the hours:')
hour = eval(input())

print('Enter the minutes:')
minute = eval(input())

print('Enter the seconds:')
second = eval(input())

if ((0<= hour < 24) and (0 <= minute <60) and (0<= second <60)):
    print('Your time is valid.')
else:
    print('Your time is invalid.')