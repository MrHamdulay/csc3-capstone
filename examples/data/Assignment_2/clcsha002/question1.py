def leap_year():
    if (years%400 == 0)or (years%100 !=0) and (years%4==0):
        print (years, "is a leap year.")
    else:
        print(years, "is not a leap year.")
years=eval(input("Enter a year: \n"))
leap_year()
