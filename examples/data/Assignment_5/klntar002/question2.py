# tarisai kalinde
# klntar002
# program to simulate a vending machine, giving change and shit


def vendingmachine():
    #user is now inputing the cost and the deposit in cents
    
    cost=eval(input('Enter the cost (in cents):\n'))
    if cost>0:
        deposit=eval(input('Deposit a coin or note (in cents):\n'))
        # while loop for the deposit just incase deposit does not meet the amount cost
        while deposit < cost:
            deposit2=eval(input('Deposit a coin or note (in cents):\n'))
            
            deposit=deposit+deposit2 # deposite accumulation
        
       
    
        # calculation of change
        change=deposit-cost
        # change distribution
        if change>0:    
            print('Your change is:')
        
        a=change//100
        if a>0:
            print(a,'x $1')
        b=change%100
        if b>0:
                c=b//25
                if c>0:
                    print(c,'x 25c')
                d=b%25
                if d>0:
                        e=d//10
                        if e>0:
                            print(e,'x 10c')
                        f=d%10
                        if f>0:
                                g=f//5
                                if g>0:
                                    print(g,'x 5c')
                                h=f%5
                                    
                                if h>0:
                                        i=h//1
                                        if i>0:
                                            print(i,'x 1c')
                
                
         
    
    
    #print(change_money)
    
vendingmachine()
    
    
    
    
        
        
