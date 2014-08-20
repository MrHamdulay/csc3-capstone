# Program to determine if a year was a leap year
# Nomsa Gamedze
# 7 March 2014

year = eval(input("Enter a year:"'\n'))

def main():
    if year%400==0:
        print(year, "is a leap year.")
    elif year%4 ==0:
        if year%100!=0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is not a leap year.")
    

main()