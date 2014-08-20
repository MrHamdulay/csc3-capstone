year = eval(input("Enter a year:\n"))

if (year%400 == 0):
    print("%d is a leap year." % (year))
elif ((year% 4 == 0) and (year%100 != 0)):
    print("%d is a leap year." % (year))
else:
    print("%d is not a leap year." % (year))