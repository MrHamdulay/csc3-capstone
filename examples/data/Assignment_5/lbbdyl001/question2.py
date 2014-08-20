"""a vending machine that prints exact change
By Dylan
April 17th 2014"""

def vend():
    cost = eval(input ( "Enter the cost (in cents):"'\n' ))
    dep = 0
    if cost == 0:
        print()
    while dep < cost:
        dep += eval( input ( "Deposit a coin or note (in cents):"'\n' ))
    change = dep - cost
    if change == 0:
        print()
    dollar = change // 100
    change -= dollar*100
    quart = change // 25
    change -= quart*25
    dime = change // 10
    change -= dime * 10
    nickel = change // 5
    change -= nickel * 5
    penny = change // 1
    finder = 0
    print("Your change is:")
    for i in range (5):
        cur = ( dollar, quart, dime, nickel, penny )
        symbol =  ("$1", "25c", "10c", "5c", "1c")
        if cur[i] == 0:
            continue
        else:
            print (cur[i], 'x', symbol[i])
        
if __name__=="__main__": 
    vend()     
            
        
    
    