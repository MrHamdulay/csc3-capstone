#Assignment 2: Question 1:
#Author: Adam Howa
#date 06/03/2014
year = eval(input("Enter a year:\n"))
if (year%100 == 0):
   if (year%400==0):
      print(year,"is a leap year.")
   else:
      print(year,"is not a leap year.")
else:
   if(year%4 == 0):
      print(year,"is a leap year.")
   else:
         print(year,"is not a leap year.")