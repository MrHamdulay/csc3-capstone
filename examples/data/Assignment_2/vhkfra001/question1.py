# Program that determines whether of not a year is a leap year

year = eval(input("Enter a year:\n") )

rem400 = year%400
rem4 = year%4
rem100 = year%100

if rem400 == 0:
    print (year, "is a leap year.")
    
elif (rem4 == 0) and (rem100 != 0):
    print (year, "is a leap year.")
    
else:
    print (year, "is not a leap year.")
    
    


            