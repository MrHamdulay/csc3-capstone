# Program that check if a inout year is leap or not
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 14/03/2014

year = eval(input('Enter a year:\n'))

if (year%400)==0 or (year%4==0 and year%100!=0):
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')