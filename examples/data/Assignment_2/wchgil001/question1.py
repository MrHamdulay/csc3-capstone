x=eval(input('Enter a year:\n'))
x/400
x/4
x/100
if (x%400==0) or (x%4==0) and (x%100!=0):
    print(x,'is a leap year.')
else:
    print(x,'is not a leap year.')