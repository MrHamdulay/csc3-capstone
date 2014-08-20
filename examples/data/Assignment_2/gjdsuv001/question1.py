#Program to determine a leap year
#Written by: Suvir Gajadhur
#3 March 2014


x = eval(input("Enter a year: \n"))

if x%400 == 0:
    print(x, "is a leap year.")
    
elif x%4==0 and x%100 != 0:
    print(x, "is a leap year.")
    
else:
    print(x, "is not a leap year.")
    
    
    
            