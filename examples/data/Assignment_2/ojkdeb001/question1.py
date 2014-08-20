# Deborah Ojuka
# Program to check if year is a leap year

year = eval(input("Enter a year: \n"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0) :
    print(year, "is a leap year.",sep=" ")
else: print(year, "is not a leap year.")