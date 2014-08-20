'''vending machine simulation
Author: Raees Elnad
Date: 14 April 2014'''

import math
#Ask user for cost
x=eval(input('Enter the cost (in cents):\n'))
if x>0: # Cost must be positive
    #Ask user for Deposit
    y=eval(input('Deposit a coin or note (in cents):\n'))    
    if y>=0: # Deposit must be equal or greater than 0
        
        # calculates change
        z=x
        if y<x:
            while y<x:
                z=eval(input('Deposit a coin or note (in cents):\n'))
                y+=z
        if y>x:
            c=y-x
        elif y==x:
            c=0
        
        if c!=0:
            print('Your change is:')
            t=0
            
            # Determines the amount of money you need
            if c!=0:
                if c!=0 and c>=100:
                    while c>=100:
                        c-=100
                        t+=1
                    print(t,'x','$1')
                    t=0
                if c!=0 and 100>c>=25:
                    while 100>c>=25:
                        c-=25
                        t+=1 
                    print(t,'x','25c')
                    t=0
                if c!=0 and 25>c>=10:
                    while 25>c>=10:
                        c-=10
                        t+=1
                    print(t,'x','10c')
                    t=0
                if c!=0 and 10>c>=5:
                    while 10>c>=5:
                        c-=5
                        t+=1
                    print(t,'x','5c')
                    t=0
                if c!=0 and 5>c>=1:
                    while 5>c>=1:
                        c-=1
                        t+=1 
                    print(t,'x','1c')
                
    

        
   
        
     