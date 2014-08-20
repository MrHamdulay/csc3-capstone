#a programme that calculate change on a vending machine:
#maisha Ivha 
#15 April 20114

#W REFERS TO CHANGE 
w=[100,25,10,5,1]
y=["$1","25c","10c","5c","1c"]

def change():
    cost=int(input("Enter the cost (in cents): \n"))
    a=0
    if cost==0:
        return
    while True:        
        deposit=int(input("Deposit a coin or note (in cents): \n"))
        a=a+deposit      
        if a>= cost:
            break
    d=a-cost
    if d==0:
        return
    print("Your change is:")
    for i in w:
        s=d//i
        if s>0:
            
            print(s,"x",y[w.index(i)])#indexing the list in w
            #the index from Wis used to index y so that change can be given with units
            d=d%i#assigning the remeinder to be our new change for our new iteration
    
change()