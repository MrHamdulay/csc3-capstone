# A program to determine whether a year is a leap year or not
# Xola Bilose
# 09/03/2014
year = eval(input("Enter a year:\n"))    #Promting user to enterthe year to be checked
remainder1 = year%4                      # Checking if year is divible by 4 - step1
remainder = year%100
remainder2 = year%400
if remainder1 == 0 and remainder != 0:  
    print(year,"is a leap year.")
elif remainder2 == 0:
    print(year,"is a leap year.")
elif remainder == 0 and remainder2 =='True':
    print(year, "is not a leap year.")
else: print( year,"is not a leap year.")