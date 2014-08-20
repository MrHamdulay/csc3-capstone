year = int(input("Enter a year:\n"))
leap = False
if not year % 400:
    leap = True
elif year % 100 and not year % 4:
    leap = True
    
if leap:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")