def leap_year():
    year_num=eval(input("Enter a year:\n"))
    if year_num%400==0:
        print(year_num,"is a leap year.")
    elif year_num%4==0:
        if year_num%100!=0:
            print(year_num,"is a leap year.")
        else:
            print(year_num,"is not a leap year.")
    else:
        print(year_num,"is not a leap year.")
leap_year()