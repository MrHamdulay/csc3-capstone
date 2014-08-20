# A program to determine whether a year is a leap year or not.
# By: Josephine Ngoase
# 12 March 2014

year = int(input("Enter a year: \n"))
if (year % 4) == 0:
   if (year % 100) == 0:
      if (year % 400) == 0:
         print(year,"is a leap year.")
      else:
         print(year,"is not a leap year.")
   else:
      print(year,"is a leap year.")
else:
   print(year,"is not a leap year.")