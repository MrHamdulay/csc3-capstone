# question.py
# Author: DOminic Manthoko
# 09 March 2014

def leapYR():
   year = eval(input("Enter a year: \n"))
   leap0_remainder = year%400   
   leap1_remainder = year%4  
   leap1_1_remainder = year%100 
   
   if leap0_remainder == 0 or (leap1_remainder == 0 and leap1_1_remainder != 0):
      print(year,"is a leap year.")
   else:
      print(year,"is not a leap year.")
            
leapYR()