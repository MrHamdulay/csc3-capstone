year = int(input("Enter a year:\n"))
print(str(year) + (" is " if (year%400==0 or (year%4==0 and year%100!=0)) else " is not ") + "a leap year.")
