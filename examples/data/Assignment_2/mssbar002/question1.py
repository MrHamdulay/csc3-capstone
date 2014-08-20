# Assignment 2. Question 1
# A program to determine whether a year is a leap year or not. 
# A year is a leap year if 
# (a) it is divisible by 400 or 
# (b) it is divisible by 4 but not by 100.

# Author: Barnett msiska(MSSBAR002)
# Date: 07/03/2014

def main():
    # Request User Input
    year = eval(input("Enter a year:\n"))
    
    #Process and Output
    if (year%400) == 0:
        print(year, "is a leap year.")
    elif (year%4) == 0 and (year%100) != 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
        
main()