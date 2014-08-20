# Shanice Sewnarain
# SWNSHA007
# 7 March 2014
# A program to determine whether a year is a leap or not
import math      # Makes the math library available. 
def main():
 x= eval(input("Enter a year: \n"))
 if x%400==0:
    print(x,"is a leap year.")
    
 elif x%4==0 and x%100!=0:
  print(x,"is a leap year.")
  
 else:
    print(x, "is not a leap year.")
     
main()  
            
          
              
