# question1.py
# Mufudzi Nhamoinesu
# Program to determine whether a year is a leap year or not

import math
year = eval(input("Enter a year:\n"))
if year%400 == 0:
 print(year,"is a leap year.")
elif year%4==0:
 print(year,"is a leap year.")
elif year%100==0:
  print (year,"is not a leap year.")
else:
 print(year, "is not a leap year.")