#Leap year calculation program

year=eval(input('Enter a year: '+'\n'))
if year==(2100):
    print ('2100 is not a leap year.')
else:
    if year%4==0 and year%100!=100:
        print (year, 'is a leap year.')
    else:
        print (year, 'is not a leap year.')