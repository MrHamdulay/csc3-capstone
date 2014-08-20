# Cherise Dube
# 11 March 2011
#Program to find out whether a year is a leap year

def leap_year ():
    x=eval(input("Enter a year:\n"))
    if x%400==0: print (x,"is a leap year.") 
    elif x%4==0 and x%100>0: 
        print (x,"is a leap year.")
    else: print (x,"is not a leap year.")
leap_year ()