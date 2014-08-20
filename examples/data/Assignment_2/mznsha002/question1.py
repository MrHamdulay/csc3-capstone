#Calculating the whether a year is a leap year or not
#11 March 2014
def main():
    year= (eval(input("Enter a year:\n")))
    year_calc4 = year%4 
    year_calc100 = year%100
    
    
    if (year == 2000):
        print(year, "is a leap year.")  
    else:
        if year_calc4 == 0 and year_calc100 != 0:           
            print(year, "is a leap year.")  
        else:
            print(year, "is not a leap year.")

main()