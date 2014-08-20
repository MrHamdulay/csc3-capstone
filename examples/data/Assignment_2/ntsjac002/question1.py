Year=eval(input("Enter a year:\n"))
if (Year%400==0) or (Year%100!=0) and (Year%4==0) :
    print(Year,"is a leap year.")
else :
    print(Year,"is not a leap year.")