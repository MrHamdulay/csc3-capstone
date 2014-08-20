#Assignment 2, Question 1
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 08/03/2014

#The program is designed to determine whether a specific year is a leap year or not.

#Pre-condition: Input year.
#Post-condition: Output type of year.

#Defining function leapYear() to check year.
def leapYear():
    year = eval(input("Enter a year:\n"))
        
    if(year%4==0):
        if(year%100 != 0):
            print(year,"is a leap year.")
        
        elif(year%400 != 0):
            print(year,"is not a leap year.")
        
        else:
            print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")

leapYear()