x = eval(input("Enter a year:\n"))

if x%4==0 and x%100!=0:
        print(x, "is a leap year.")
if x%400==0:
        print(x, "is a leap year.")
if x%4!=0:
    print(x, "is not a leap year.")
if x == 2100 or x == 1900:
        print(x, "is not a leap year.")