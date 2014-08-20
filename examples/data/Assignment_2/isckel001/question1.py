# A program to determine leap years
# Done by Kelly Isaacs
# 10-03-2014

# Defining input values

year=eval(input("Enter a year:\n"))


# Using rules given to establish whether input value is a leap year

if year%400==0 or year%4==0 and year%100!=0 : # Remainder guidelines
    print(year,"is a leap year.")
    

# Anything other than guidelines made must use:

else: print(year,"is not a leap year.")  

