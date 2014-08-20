#programme to simulate a vending machine 
#takunda chikondo 
#13 apr 2014
x =eval(input("Enter the cost (in cents):\n"))
y = 0
if x>0:
    y=eval(input("Deposit a coin or note (in cents):\n"))
    
#asks user to add extra till deposit is equal or greater than cost
    while x>y :
        z=eval(input("Deposit a coin or note (in cents):\n"))
        y+=z
#calucates the change
    else:
        change=y-x
        if x!=y:
            print("Your change is:")
            if change//100!=0:
                a=change//100
                print(a,"x $1")
                change-=(a*100)
    
            if change//25!=0:
                b=change//25
                print(b,"x 25c")
                change-=(b*25)
    
            if change//10!=0:
                c=change//10
                print(c,"x 10c")
                change-=(c*10)
                    
            if change//5!=0:
                d=change//5
                print(d,"x 5c")
                change-=(d*5)
            
            if change//1!=0:
                e=change//1
                print(e,"x 1c")
            
            
            


        
        
        
    
    
    

    




