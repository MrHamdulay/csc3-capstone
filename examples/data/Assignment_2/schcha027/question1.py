def leapYear(yr):
    if(yr%400==0) or (yr%4==0 and not yr%100==0):
        print(yr,"is a leap year.")
    else:
        print(yr,"is not a leap year.")

yr=eval(input("Enter a year:\n"))    
leapYear(yr)
