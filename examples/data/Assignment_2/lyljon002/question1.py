#8 March 2014
#Assignment 2, Question 1
#Jonathan Leyland, LYLJON002


year = eval(input("Enter a year:\n"))

leapyear = bool
leapyear = False

if year % 400 == 0:
    leapyear = True


if (year % 4 == 0) and (year % 100 != 0):
    leapyear = True
    
if leapyear == True:
    print(year, "is a leap year.")
else: print(year, "is not a leap year.")