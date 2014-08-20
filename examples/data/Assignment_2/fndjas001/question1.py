#A program to determine if a year is a leap year or not
#Jason Findlay
#14/03/2014

x=eval(input('Enter a year:\n'))

if x/400 == x//400 or (x/4 == x//4 and x//100 - x/100 != 0):
    print(x, 'is a leap year.')
else:
    print(x, 'is not a leap year.')
    
