def isLeapYear():
    year = eval(input("Enter a year:\n"))
    leap_year = False
    if(year%4 == 0):
        leap_year = True
        if(year%100 == 0):
            leap_year = False
            if(year%400 == 0):
                leap_year = True
    
    if(leap_year == True):
        print(year, "is a leap year.")
    elif(leap_year == False):
        print(year, "is not a leap year.")
        
isLeapYear()