# program to determine whether it is a leap year or not
# by wilsan xubuzani

year = eval(input("Enter a year:\n"))
if (year%4 ==0 or year%400 ==0) and year%100!=0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")