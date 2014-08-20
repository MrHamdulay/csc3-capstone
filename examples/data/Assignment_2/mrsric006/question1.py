#Creator: Richard Marais
#date: 13 March 2014

import math    #import maths functions
def leapyear():
    if (leapyear1%400==0):      #test for 0 remainder 
        print(leapyear1,'is a leap year.')
    else:
        if (leapyear1%4==0) and (leapyear1%100>0):   #test for 0 remainder when divided by 4 an remainder when divided by 100
            print(leapyear1,'is a leap year.')
        else:
            print(leapyear1,'is not a leap year.')     #if conditions not met
            
leapyear1 = eval(input('Enter a year:\n'))    #answer display

leapyear()
        
        
    