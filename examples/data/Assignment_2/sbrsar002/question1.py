# Sarayn Subroyen
# 12 March 2014
# a program to determine a leap year

def main():
    year = eval(input("Enter a year:\n"))
    
    if (year%400==0) or (year%4==0) and (year%100 != 0):
        print(year,"is a leap year.")
    
    else:
        print(year,"is not a leap year.")
        
main()
