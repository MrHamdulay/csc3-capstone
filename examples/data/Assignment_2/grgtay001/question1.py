#Tayla George
#Program to determine if a year is a leap year or not
# 7 March 2014

year = eval(input("Enter a year:\n"))
def leap(year):
    if (year%400)==0 or (year%4)==0 and (year%100!=0): 
        print(year,"is a leap year.")
    elif (year//4) + (year%100)>0:
        print(year,"is not a leap year.")
leap(year)