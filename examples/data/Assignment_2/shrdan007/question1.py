year = eval(input("Enter a year:\n"))

x = year

if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
    print(year, "is a leap year.")
    
else:
    print(year, "is not a leap year.")
        
        
    







