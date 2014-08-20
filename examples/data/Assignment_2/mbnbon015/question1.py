#program to to point out wheather a year is a leap year or not
year=eval(input("Enter a year:\n"))
if((year%400)==0 and (year%4)==0 and (year%100)!=0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
    