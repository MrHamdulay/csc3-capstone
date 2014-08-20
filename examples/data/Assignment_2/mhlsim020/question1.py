#A program to determine whether a year is a leap year or not.
#Simlindile Mahlaba
# 14 March 2014

x = int(input("Enter a year:\n"))
if (x % 4) == 0:
   if (x % 100) == 0:
      if (x % 400) == 0:
         print(x, "is a leap year.")
      else:
         print(x, "is not a leap year.")
   else:
      print(x, "is a leap year.")
else:
   print(x, "is not a leap year.")