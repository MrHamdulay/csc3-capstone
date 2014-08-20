# question1.py
#  A program to determine if a year is a leap year or not 

import math 

def main():
    x = eval(input("Enter a year:\n"))
    if (x%400)==0:
        print(x,"is a leap year.")
    elif (x%4)==0 and (x%100)>0:
        print(x,"is a leap year.")
    else:
        print(x,"is not a leap year.")

    
main()  

            