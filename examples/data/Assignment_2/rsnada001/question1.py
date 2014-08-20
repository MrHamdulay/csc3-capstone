#RSNADA001
#Adam Rosendorff
year = eval(input('Enter a year:\n'))
leap = False
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    leap = True
print(year,' is ','not '*(not leap),'a leap year.',sep='')

