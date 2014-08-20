#Aiden Walton
#Program to determine whether a year is a leap year or not

def leapyear(year):
    if year%400==0 or year%4==0 and year%100!=0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
        
year=eval(input("Enter a year:\n"))
leapyear(year)