"""Vending machine program
Tameryn Pillay
15 April 2014"""

def vend_machine():
    
    # cost of item
    cost=eval(input("Enter the cost (in cents):\n"))
    my_money=0
    
    while cost > my_money:
        received=eval(input("Deposit a coin or note (in cents):\n"))
        my_money += received
        if my_money == cost:
            print("")
           
        elif my_money > cost:
            change= my_money-cost
            
            #Calculating change
            dollar=change//100
            quarter=(change%100)//25
            ten=((change%100)-(quarter*25))//10
            five=((change%100)-(quarter*25)-(ten*10))//5
            cent=((change%100)-(quarter*25)-(ten*10)-(five*5))
            
            print("Your change is:")
            if dollar!= 0:
                print(dollar ,"x $1")
            if quarter!= 0:
                print(quarter,"x 25c")
            if ten!= 0:
                print(ten,"x 10c")
            if five!= 0:
                print(five,"x 5c")
            if cent!= 0: 
                print(cent,"x 1c")            
            
            
vend_machine()      