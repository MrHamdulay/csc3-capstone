year = eval(input("Enter a year:\n"))
leap = False
##is year leap?
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    leap = True
else:
    leap = False
##output
if leap == True:
    print(year,"is a leap year", sep=" ", end = ".")
elif leap == False:
    print(year,"is not a leap year", sep=" ", end = ".")
    