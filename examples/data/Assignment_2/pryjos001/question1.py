#Program to evaluate whether or not a year is a leap year

year = eval(input("Enter a year:\n"))
if year%400==0 or year%4==0 and year%100>0: #If year is divisible by 400 or if year is divisible by 4 and not divisible by 100
    print((year), "is a leap year.")
else: print ((year), "is not a leap year.")