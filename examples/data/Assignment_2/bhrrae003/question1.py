#Raeesa Behardien
#Assignment 2
#BHRRAE003

#Question 1
#Programme to determine whether a year is a leap year or not.

yr = input("Enter a year:" '\n')
yr = eval(yr)
import math
if (yr%400==0) or (yr%4==0 and yr%100!=0):
    print( yr,"is a leap year.")
else:
    print( yr,"is not a leap year.")
    
    
    
    