year=eval(input("Enter a year:\n"))

if(year%400==0):
    print(year, "is a leap year.", end='')

elif(year%4==0 and year%100>0):
    print(year, "is a leap year.", end='')
else:
    print(year, "is not a leap year.",end='')