year=eval(input("Enter a year:\n"))
remainder1 = year%400
remainder2 = year%4
remainder3= year%100

if (remainder1 == 0) or ((remainder2 == 0) and (remainder3 != 0)):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")