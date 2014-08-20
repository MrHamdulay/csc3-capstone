#ASSIGNMENT 2
#QUESTION 1
#WHTBAS001
#BASIL T WHITEHEAD
#10-03-2014

def leap():
    year = eval(input("Enter a year: "))
    print()
    if year % 400 == 0:
        print(year, "is a leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
        
leap()