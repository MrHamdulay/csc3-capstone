#Program to determine whether a year is a leap year or not.
#Tsanwani Vhonani
#09 March 2014

def Leap_year():
    year=eval(input("Enter a year:\n"))
    if year%400==0:
        print(year,"is a leap year.")
    elif year%100==0:
        print(year,"is not a leap year.")
    elif year%4==0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
        
Leap_year()

