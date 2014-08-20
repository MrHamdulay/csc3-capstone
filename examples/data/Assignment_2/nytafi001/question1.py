# A program to determine whether a year is a leap year or not
# Author: Afika Nyati
# 9 March 2014

def main():
    
    try:
        currentyear = eval(input("Enter a year:\n"))
        
    
        if (currentyear%400 == 0 or (currentyear%4 == 0 and currentyear%100 != 0)):
            print(currentyear, "is a leap year.")
        
        else:
            print(currentyear, "is not a leap year.")
    
    except NameError:
        print("You did not type in a number, please type the year as a numerical value only.")
        
main()
        