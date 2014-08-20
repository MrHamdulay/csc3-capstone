print('Enter a year:')
year=eval(input())
if (year%400)==0 or (year%4)==0 and (year%100!=0):
    print(year,'is a leap year.')
elif (year//4) + (year%100)>0:
    print(year,'is not a leap year.')
    
 
        