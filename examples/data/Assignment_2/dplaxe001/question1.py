year = eval(input("Enter a year:\n"))
leap = year%4
if year == 2100:
    print(year, "is not a leap year.")
else:
    if leap == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")    
