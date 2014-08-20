year = eval(input("Enter a year:\n"))

a = 0
if year//4==year/4 and year//100!=year/100:
    a = 1
if year/400==year//400 or a==1:
    print(year,"is a leap year.")
    
else:
    print(year,"is not a leap year.")