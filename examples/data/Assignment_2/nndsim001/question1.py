# This program determines if a year entered by the user is a leap year

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 11 March 2014


year = eval(input("Enter a year:\n"))


# A year is a leap year if it is divisible by 400 or 4 and not by 100

if (year%400 == 0 or year%4 ==0) and year%100 !=0:
    print(year,"is a leap year.")
else:
    if (year%2000 == 0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")



#Sample I/O:

#Enter a year:
#2008
#2008 is a leap year.

#Sample I/O:

#Enter a year:
#2009
#2009 is not a leap year.