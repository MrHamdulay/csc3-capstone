k=eval(input('Enter a year:\n'))
if k%4==0 and k%100!=0 or k%400==0:
    print(k,'is a leap year.')
else: print(k,'is not a leap year.') 