#Program to determine if a year is a leap year or not
#Christopher Betteridge
#BTTCHR004
#Assingment 2; question 1 - 09/03/2014

year = eval(input("Enter a year:\n"))
if (year%4==0 and year%100>0) or (year%400==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")