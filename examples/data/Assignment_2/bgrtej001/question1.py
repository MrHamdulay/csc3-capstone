#Assignment 2, Question 1
#Tejasvin Bagirathi BGRTEJ001
#11/03/2014

def leapYear():
    year=eval(input("Enter a year:\n"))
    if year%400 == 0:
        print(year,"is a leap year.")
    elif year%100 != 0 and year%4 == 0:
        print(year, "is a leap year.")
    else: print(year,"is not a leap year.")
    
leapYear()