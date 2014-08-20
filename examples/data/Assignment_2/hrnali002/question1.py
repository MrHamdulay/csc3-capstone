#A program to determine whether or not it is a leap year
#Alison Hoernle
#HRNALI002
#8 March 2014

year=eval(input("Enter a year:\n"))
if (year % 400 == 0):
    print(year,"is a leap year.")
elif (year % 100 != 0 and year % 4 == 0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")