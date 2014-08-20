"""Vending machine
Julia Breakey
15 April 2014"""

#get cost
cost=eval(input("Enter the cost (in cents):\n")) 

#ask for money like the golddigger you are
dep=0
total=0
while total<cost:
    dep=eval(input("Deposit a coin or note (in cents):\n"))
    total=total+dep

#evaluate change    
change=total-cost

print("Your change is:") #alert them that the money coming out is in fact only their change and they did not just win at slots
if change%100==0:
    print(change//100, "x $1") #if the change only needs dollars
else:
    a=change//100     #int division to get dollars otherwise
    if a!=0:
        print(a, "x $1")
    change=change-a*100  #change becomes less
    if change%25==0:
        print(change//25, "x 25c") #if only $ and 25c
    else:
        b=change//25        #and so on
        c=change%25
        if b!=0:
            print(b, "x 25c")
        change=change-b*25
        if c%10==0:
            print(c//10, "x 10c")   
        else:
            c=change//10    #and so forth 
            d=change%10
            if c!=0:
                print(c10, "x 10c")
            change=change-c*10      #for all of the coins
            if d%5==0:
                print(d//5, "x 5c")
            else:
                d=change//5
                e=change%5
                if d!=0:
                    print(d, "x 5c")
                if e!=0:
                    print(e, "x 1c")    #happy days