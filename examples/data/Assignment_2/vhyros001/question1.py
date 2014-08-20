# Ross van der Heyde VHYROS001
# Assignment 2 question 1
# 8 March 2014
# Determines whether a year entered is a leap year or not

year = eval(input('Enter a year:\n'))# ask user for year

if year % 400 ==0 or year % 4==0 and year % 100 !=0:
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')