# Question 2 in Assignment 1
# Author: Julius Stopforth
# Date: 26/02/2014

hours = int(input('Enter the hours:\n'))
minutes = int(input('Enter the minutes:\n'))
seconds = int(input('Enter the seconds:\n'))

if not((0<=hours<=23) and (0<=minutes<=59) and (0<=seconds<=59)):
    print('Your time is invalid.')
else:
    print('Your time is valid.')