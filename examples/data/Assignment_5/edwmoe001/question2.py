import sys
import os
def dlr(change):
    global x
    if change == 0: 
        return
    else:
        print("Your change is:")
        if change >=100:
            dollar = change/100
            if dollar < 10:
                dollaramt = str(dollar)[0]
                print(dollaramt,"x","$1")
                x = change - (int(dollaramt) * 100)
            else:
                dollaramt = str(dollar)[0:2]
                print(dollaramt,"x","$1")
                x = change - (int(dollaramt) * 100)            
        else:
            return
    

def qtr(change):
    global x
    if int(change) <= 0:
        return
    else:
        if change >= 25:
            qtr = change/25
            qtramt = str(qtr)[0]
            print(qtramt,"x","25c")
            x = change - (int(qtramt) * 25)
           
        else:
            return    

def ten(change):
    global x
    if int(change) <= 0:
        return
    else:    
        if change >= 10:
            ten = change/10
            tenamt = str(ten)[0]
            print(tenamt,"x","10c")
            x = change - (int(tenamt) * 10) 
            return change
                
        else:
            return    

def five(change):
    global x
    if int(change) <= 0:
                    return
    else:    
        if change >= 5:
            five= change/5
            fiveamt = str(five)[0]
            print(fiveamt,"x","5c")
            x = change - (int(fiveamt) * 5)
            return change
        else:
            return

def one(change):
    global x
    if change <= 0:
                    return
    else:    
        if change >= 1:
            one = change/1
            oneamt = str(one)[0]
            print(oneamt,"x","1c")
            x = change - (int(oneamt) * 1)
            return change
            
        else:
            return
    
def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    amount = 0 
    while cost > amount: 
        dep = eval(input("Deposit a coin or note (in cents):\n"))
        amount = amount + dep
    global x
    x = amount - cost
    dlr(x)
    qtr(x)
    ten(x)
    five(x)   
    one(x)
    
 
        
                
main()
