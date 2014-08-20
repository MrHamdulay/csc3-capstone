# program to enter coins in a vending machine and display change
# by Jacob Mwanza
# 15/04/2014


def cost():
    #enter cost of of item
    x = eval(input("Enter the cost (in cents):\n"))
    y = 0
    
    while y < x:
        z = eval(input("Deposit a coin or note (in cents):\n"))
        y += z
        
        if y > x:
            # calculate change
            change = y - x
            print('Your change is:')
            calc_change(change)
    
        elif y > x:
            #calculate change
            change = y - x
            print('Your change is:')
            calc_change(change)
    

# distribute calculated change            
def calc_change(p):
    
    # calculate dollars
    a = p//100
    if a != 0:
        print(a,'x $1')
        
    # calculate quarters
    b = (p - (a*100))//25
    if b !=0:
        print(b,'x 25c')
        
    # calculate 10c
    c = (p - (a*100 + b*25))//10
    if c != 0:
        print(c,'x 10c')
        
    # calculate 5c
    d = (p - (a*100 + b*25 + c*10))//5
    if d != 0:
        print(d,'x 5c')
        
    # calculate 1c to 4c
    e = (p -(a*100 + b*25 + c*10 + d*5))
    if e != 0:
        print(e,'x 1c')  
            
cost()