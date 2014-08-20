# vending machine program
# Sohail Tulsi TLSSOH001
# 17 April 2014

val = eval(input('Enter the cost (in cents):\n')) # cost of item
taken = 0
# restriction until enough money is intaken
while taken < val:
    intake = eval(input('Deposit a coin or note (in cents):\n'))
    taken+=intake
    
change=taken-val
dol1=0
c25=0
c10=0
c5=0
c1=0
# calculateing change 
while change>0:
    print('Your change is:')
    
    if change/100 >=1:
        dol1=change//100
        change= change-(dol1*100)
   
    if change/25 >=1:
        c25=change//25
        change= change-(c25*25)  
   
    if change/10 >=1:
        c10=change//10
        change= change-(c10*10) 
    
    if change/5 >=1:
        c5=change//5
        change= change-(c5*5)    
        
    if change/1 >=1:
        c1=change//1
        change= change-c1
# printing change given        
if dol1:
    print(dol1,'x $1')
if c25:
    print(c25,'x 25c')    
if c10:
    print(c10,'x 10c')
if c5:
    print(c5,'x 5c')        
if c1:
    print(c1,'x 1c')        
        
        