#Program to determine if year is a leap year
#Shivam Ragoonaden
#6 March 2014

Y = eval(input("Enter a year:\n"))

Valid = False

if (Y % 400 == 0) or (Y % 4 == 0) and (Y % 100 > 0):
    Valid = True

Y = str(Y)
if Valid == True:
    print(Y,"is a leap year.")
else:
    print(Y,"is not a leap year.")    
