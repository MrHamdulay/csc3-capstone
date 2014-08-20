# a program to determine whether a year is a leap year or not.
# BDGMUL001
# Badugela Mulisa
# 08 March 2014

def main():
        year = eval(input('Enter a year:\n'))
         
        if year%400==0:
                print(year, "is a leap year.")
        elif year%100==0:
                print(year, "is not a leap year.")
        elif year%4==0:
                print(year, "is a leap year.")
         
        else:
                print(year, "is not a leap year.")
             
    
         

main()