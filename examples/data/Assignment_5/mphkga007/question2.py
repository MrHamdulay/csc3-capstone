def vending_machine():
    cost=eval(input("Enter the cost (in cents):\n"))
    if cost>0:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        while deposit<cost:
            deposit2=eval(input("Deposit a coin or note (in cents):\n"))
            deposit=deposit+deposit2
        change=deposit-cost
        if change!=0:
            print("Your change is:")
            cents=[100,25,10,5,1]
            convert=""
            for i in cents:
                div=change//i
                if div==0:continue
                remain=change%i
                
                if i//100!=0:
                    i=i//100
                    i=str(i)
                    i="$"+i
                else:
                    i=str(i)
                    i=i+"c" 
                div=str(div)
                i=str(i)        
                                
                convert=convert+div+" "+"x"+" "+i+"\n"
                div=int(div)
                            
                change=remain
                #if change==0:break                
            
                
            print(convert)

  
        
        

vending_machine()
    
    
        
        