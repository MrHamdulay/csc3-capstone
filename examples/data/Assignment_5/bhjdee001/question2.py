#deepak
#q2 - vending machine

cost=eval(input("Enter the cost (in cents):\n"))
moneyIn=0
while moneyIn < cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    moneyIn+=deposit

change=moneyIn-cost
#print(change)
dollar=0
c25=0
c10=0
c5=0
c1=0


while change>0:
    print("Your change is:")
    
    if change/100 >=1:
        dollar=change//100
        change=change-(dollar*100)
    
    if change/25 >=1:
        c25=change//25
        change=change-(c25*25)
    
    if change/10 >=1:
        c10=change//10
        change=change-(c10*10)  
            
    if change/5 >=1:
        c5=change/5
        change=change-(c5*5)
    
    if change/1 >=1:
        c1=change//1
        change=change-(c1*1)
        

#division of change
if dollar:
    print(dollar,"x $1")
if c25:
    print(c25,"x 25c")
if c10:
    print(c10,"x 10c")
if c5:
    print(c5,"x 5c")
if c1:
    print(c1,"x 1c")