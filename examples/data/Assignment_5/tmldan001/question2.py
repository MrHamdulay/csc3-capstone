'''Program to simulate a vending machine and calculate change based on the amount paid
Daniel M. Tamale
TMLDAN001
2014-04-15'''

def vender():
    total_amount=0
    change=0

    '''Amount requested by the vending machine'''
    while True: 
        cost=eval(input('Enter the cost (in cents):\n'))
        if cost>=0:
            break
    
    '''Amount deposited by the buyer in reference to required amount'''
    while True:
        amount=eval(input('Deposit a coin or note (in cents):\n'))
        total_amount+=amount
        if total_amount>=cost:
            break
        
        '''Vending machine checking and giving change'''
    change=total_amount-cost
    if change>0:
        print ('Your change is:\n',end='')
    if change>=100:
        amount_2= str(change//100) + ' x $1'
        print (amount_2)
        change=change-((change//100)*100)
    if change>=25:
        amount_3= str (change//25) + ' x 25c'   
        print (amount_3)
        change=change-((change//25)*25)
    if change>=10:
        amount_4= str (change//10) + ' x 10c'
        print (amount_4)
        change= change-((change//10)*10)
    if change>=5:
        amount_5= str (change//5) + ' x 5c'
        print (amount_5)
        change=change-((change//5)*5)
    if change>=1:
        amount_6= str (change//1) + ' x 1c'
        print (amount_6)
vender()