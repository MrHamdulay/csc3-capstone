# Assignment 2
# Question 1
# A programme to determine whether or not a year is a leap year

def leapyear():
    
    year=eval(input("Enter a year:\n"))
    if (year%4==0 and year%100!=0):
        print(year,"is a leap year.")
    elif(year%400==0):
        print(year,"is a leap year.")
    else:
            print(year,"is not a leap year.")
leapyear()