
"""Simulation of a vending machine
Michelle Lu
13 April 2014"""


cost=eval(input("Enter the cost (in cents):\n"))
if cost>0:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        while deposit<cost: #asks for more money until cost has been met or exceeded
                extra=eval(input("Deposit a coin or note (in cents):\n"))
                deposit+=extra
        if deposit>cost or deposit==cost:
                change=deposit-cost 
                if change>0: #to work out the amount of change
                        print("Your change is:")
                        dollars=change//100 
                        change-=dollars*100
                        if dollars>0: #only prints out dollars if there is a value for it
                                print(dollars, "x", "$1")
                        if change>0: #continues to work out change until change is zero
                                quarters=change//25
                                change-=quarters*25
                                if quarters>0:
                                        print(quarters, "x", "25c")
                                if change>0:
                                        ten=change//10
                                        change-=ten*10
                                        if ten>0:
                                                print(ten, "x", "10c")
                                        if change>0:
                                                five=change//5
                                                change-=five*5
                                                if five>0:
                                                        print(five, "x", "5c")
                                                if change>0:
                                                        one=change
                                                        if one>0:    
                                                                print(one, "x", "1c")
