def leapyear():
    year = eval(input("Enter a year:\n"))

    rem1 = year%4
    rem2 = year%400
    rem3=year%100

    if (rem1==0 and rem3!=0):
        print(year, "is a leap year.")
    elif (rem2==0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

leapyear()