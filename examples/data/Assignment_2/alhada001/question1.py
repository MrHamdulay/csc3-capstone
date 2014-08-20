year = eval(input("Enter a year: \n"))
num = year % 400.0
num1  = year % 4.0

num2 = year % 100.0

if (num == 0) or ((num1 == 0) and (num2 != 0)):
    print(year, "is a leap year.")
else:
     print(year, ("is not a leap year."))