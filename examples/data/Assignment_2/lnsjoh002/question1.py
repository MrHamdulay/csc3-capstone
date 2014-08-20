# A program to determine whether it is a leap year or not

def leap(year):
    
    
    
    if year%400 == 0:   #if remainder when year/400 is equal to 0
        print(year, "is a leap year.")
    
    elif year%4 == 0 and year%100!=0: #year%100!=0: If year/100 not equal to 0
        print(year, "is a leap year.")
    
    else:
        print(year, "is not a leap year.")
        
year=eval(input("Enter a year: \n"))

leap(year)
    