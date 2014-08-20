def determineLeapYear(testYear):
    
    if (testYear%400==0) or (testYear%4==0 and testYear%100!=0):
        print(testYear,"is a leap year.")
    else:
        print(testYear,"is not a leap year.")
        
year = eval(input("Enter a year:\n"))    
determineLeapYear(year) 