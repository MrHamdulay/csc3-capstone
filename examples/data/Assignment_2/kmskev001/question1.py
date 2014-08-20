# program to tell if a year is a leap year
# kevin kumasamba
# question 1

year=eval(input("Enter a year:\n"))
if year%400==0: # the remainder of year has to be equal to 0 
    print(year, "is a leap year.")
elif year%4==0 and year!=2100:
    print(year, "is a leap year.")
else: 
    print(year, "is not a leap year.")
    


     