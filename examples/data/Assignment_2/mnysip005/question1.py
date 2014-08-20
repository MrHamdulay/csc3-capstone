#leap year progam
#watch out for brackets!!!!
import math 
y= eval(input("Enter a year:\n"))
#% is to find the remainder
if(y%400==0 or y%4==0 and y%100!=0 ):
    print(y,"is a leap year.")
else:
    print(y,"is not a leap year.")