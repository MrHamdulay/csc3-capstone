#assignment2 question1
year=eval(input("Enter a year:\n"))
if year/400==year//400:
    print(str(year),"is a leap year.")
elif (year/4==year//4) and (year/100!=year//100):
    print(str(year),"is a leap year.")
else:
    print(str(year),"is not a leap year.")
