#kennedy muranda
#program to determine a leap year
year=eval(input("Enter a year:\n"))
a=400
b=4
c=100
if round(year/a)==year/a or (round(year/b)==year/b and round(year/c)!=year/c):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")




