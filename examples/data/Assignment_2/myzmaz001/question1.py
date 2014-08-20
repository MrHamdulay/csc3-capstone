#07 March 2014   #Assignment2
#Mazwi Myeza     #Question1

year = eval(input("Enter a year:\n"))

if year%400 == 0 or year%4 == 0 and year%100 != 0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")