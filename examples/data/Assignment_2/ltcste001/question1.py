year=eval(input("Enter a year:\n"))
remainder =(year)%400
remainder_1=year%4
remainder_2=year%100
if remainder == 0 or (remainder_1 == 0 and remainder_2 != 0) :
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")