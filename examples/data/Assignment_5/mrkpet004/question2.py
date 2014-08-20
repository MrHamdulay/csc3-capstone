"""Vending machine simulation
peter m muriuki"""

#get inputs for cost n deposit
cost=eval(input("Enter the cost (in cents):\n"))
cash=0
change=0
while cash < cost > 0:
        cash=cash+(eval(input("Deposit a coin or note (in cents):\n")))
        if cash > cost:
                break

#determine change(if any)
if cash > cost:
        print ("Your change is:")
        change = cash-cost
        if 1<change<5:
                print (change,"x","1c",sep=" ")
        elif change>5:
                x=change//100
                y=change%100
                if x>=1:
                        print (x,"x","$1",sep=" ")
                if y>=25:
                        print ((y//25),"x","25c",sep=" ")
                y=y%25
                if y>=10:
                        print((y//10),"x","10c",sep=" ")
                y=y%10
                if y>=5:
                        print((y//5),"x","5c",sep=" ")
                y=y%5
                if 0<y<5:
                        print(y,"x","1c",sep=" ")