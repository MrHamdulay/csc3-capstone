#program to test if year is a leap year or not
year = eval(input("Enter a year:\n"))

if (year%400==0): 
    print (year,"is a leap year.");
if (year%100==0):
    print (year,"is not a leap year.");
if (year%4==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
    
