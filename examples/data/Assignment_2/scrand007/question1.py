year = eval(input("Enter a year:\n"))

if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")