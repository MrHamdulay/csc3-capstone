year = int(input("Enter a year: \n"))
div_400 = year%400
if(div_400 == 0):
    print(str(year) + " is a leap year.")
else:
    div_4 = year%4
    div_100 = year%100
    if (div_4 == 0 and div_100 != 0):
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")
