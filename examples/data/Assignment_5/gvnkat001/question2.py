#Vending Machine
#Katlego Gaveni
#15th April 2014



def vending():
    
    cost=eval(input("Enter the cost (in cents):\n"))
    paid=0
    while paid < cost: #loop that will continuously ask the customer to deposit coins until the amount deposited exeeds or is equal to the cost of the selected item
        coin=eval(input("Deposit a coin or note (in cents):\n"))
        paid+=coin
    change = paid-cost
    
    #working out how much of each coin is needed for change 
    dollar= change//100
    quater= (change-(dollar*100))//25
    ten=(change-(dollar*100)-(quater*25))//10
    five=(change-(dollar*100)-(quater*25)-(ten*10))//5
    cent=(change-(dollar*100)-(quater*25)-(ten*10)-(five*5))//1
    
    #issuing of change
    if change !=0:
        print("Your change is:")
    
        if dollar > 0:
            print(dollar,"x $1")
        if quater > 0:
            print (quater,"x 25c")
        if ten > 0:
            print (ten,"x 10c")
        if five > 0:
            print (five,"x 5c")
        if cent > 0:
            print(cent,"x 1c")
    

if __name__=="__main__":
    vending()