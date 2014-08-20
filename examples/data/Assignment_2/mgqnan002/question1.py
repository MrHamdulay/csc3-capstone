# Programme to determine whether a year is a leap year or not.
# Auther: Nangamso Mgoqi
# Date 14 March 2014

def leap_year():
   year = eval(input("Enter a year:\n"))

   if (year%4 == 0) and (year%100 !=0)  or (year%400 == 0):
      print(year, "is a leap year.")
   else:
      print(year, "is not a leap year.")
      
    

leap_year()

    
    