#Amitha Doodnath
#Student Number: DDNAMI001
#Classify year into leap year or not
#08/03/2014

year=eval(input("Enter a year:\n"))

if(year%400 == 0 or (year%4==0 and year%100 !=0)): print(year,"is a leap year.")

else: print(year,"is not a leap year.")