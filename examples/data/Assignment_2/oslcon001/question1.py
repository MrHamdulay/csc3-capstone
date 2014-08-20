#A year is a leap year if (a) it is divisible by 400 or (b) it is divisible by 4 but not by 100.
year = eval(input("Enter a year:\n"))
if year%400 ==0 or (year%4 ==0 and  year%100!=0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

            