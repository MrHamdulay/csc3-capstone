#Assignment 2, question 1
#Determines leap year
#Daniel Schwartz
#SCHDAN037
#09/03/2014
def leap():
    
    year = eval(input("Enter a year:\n"))

    if(year%400 == 0):
        print(year, "is a leap year.")
    elif(year%4 == 0):
        if(year%100 != 0):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == '__main__':
    leap()
