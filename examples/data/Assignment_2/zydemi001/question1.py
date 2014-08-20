# A program to determine whether a year is a leap year or not
# Author: Emiel Zyde
# Date: 6 March 2014

def main():
    x=eval(input("Enter a year:\n"))    #prompt the user to enter a year 
    if x%400==0:
        print(x,"is a leap year.")      #if x is divisible by 400 it is a leap year
    elif x%4==0 and x%100!=0:
        print(x,"is a leap year.")      #if x is divisbile by 4 but not by 100 it is a leap year
    else:
        print(x,"is not a leap year.")
        
main()