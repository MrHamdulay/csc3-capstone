
year = eval(input("Enter a year:\n"))
def leapyr(n):
    if (n%4!=0):
        print(n, "is not a leap year.")
    else:
        print(n, "is a leap year.")
leapyr(year)