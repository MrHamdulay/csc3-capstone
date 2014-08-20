'''vending machine program,rory welsh wlsror002'''

#loop cash input until cash is greater than or equal to cost
def payment(cost,cash):
     
    while cash < cost:
        money_payed=eval(input('Deposit a coin or note (in cents):\n'))
        cash= money_payed+cash
    
    if cash>=cost:
        change(cost,cash)
        
#calculates change
def change(cost,cash):
    change=cash-cost
    dollars=0
    cents25=0
    cents10=0
    cents5=0
    cents1=0
    
    while change>0:
        if change>=100:
            change=change-100
            dollars=dollars+1
            
        elif change>= 25:
            change=change-25
            cents25=cents25+1
            
        elif change>=10:
            change=change-10
            cents10=cents10+1
            
        elif change>=5:
            change=-5
            cents5=cents5+1
                        
        elif change>=1:
            change=-1
            cents1=cents1+1
 #displays change in coins
    if dollars>0 or cents25>0 or cents10>0 or cents5>0 or cents1 >0:
        print('Your change is:')
    if dollars>0:
        print(dollars,'x $1')
    if cents25>0:
        print(cents25,'x 25c')
    if cents10>0:
        print(cents10,'x 10c')
    if cents5>0:
        print(cents5,'x 5c')
    if cents1>0:
        print(cents1,'x 1c')
        
#enters the cost and diplays change
cost=eval(input('Enter the cost (in cents):\n'))
cash=0
payment(cost,cash)