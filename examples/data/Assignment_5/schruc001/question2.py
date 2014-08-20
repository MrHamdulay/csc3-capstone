#vending Machine Program
#Ruchaan Schmidt
#April 2014

def vendmac():
    cost = eval(input("Enter the cost (in cents):\n"))
    paidtot = 0
    change = paidtot - cost
    
    while change<0:                     
        dep = eval(input("Deposit a coin or note (in cents):\n"))
        paidtot = paidtot+dep
        if paidtot == 0:
            break
        
        if paidtot>0:
            change = paidtot - cost
            print("Your change is:")
            
            dol = (change//100)
            if dol>1:
                print(dol, "x $1")
            
            qchange = change - (dol*100)
            quart = int(qchange/25)
            if quart>0:
                print(quart, "x 25c")
            
            tencchange = change - ((dol*100)+(quart*25))
            if tenc>0:
                print(tenc, "x 10c")
            
            fivcchange = change - ((dol*100)+(quart*25)+(tenc*10))
            fivc = int(fivcchange/5)
            if fivc>0:
                print(fivc, "x 5c")
            
            singchange = change - ((dol*100)+(quart*25)+(tenc*10)+(fivc*5))
            single = int(singchange/1)
            if single>0:
                print(single, "x 1c")
vendmac()