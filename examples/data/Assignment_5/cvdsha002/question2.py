#Shahrain Coovadia
#CVDSHA002

money=eval(input("Enter the cost (in cents):\n"))

flag=True      #create boolean expression
depadd=0
add=0
while (flag==True):      
    
    if money==0:
        flag=False
        break
        
    dep2=eval(input("Deposit a coin or note (in cents):\n"))
    
    depadd=depadd-dep2               
    add=add+dep2                           
    money=money-dep2
    
    if (money<=0):
   
        change=abs(money)                              #convert to positive
    
        if change!=0:
            print("Your change is:")       

        money2=change//100

        if (money2>=1):                      #change for $1
            print(money2, "x $1")
    
        change=(change-money2*100)
    
        if change>=25:                        #change for 25c
            change25=change//25
            print(change25, "x 25c")
            change=change-change25*25
        
        if change>=10:                       #change for 10c
            change10=change//10
            print(change10, "x 10c")
            change=change-change10*10
        
        
        if change>=5:                             #change for 5c
            change5=change//5
            
            if change5>0:
                print(change5, "x 5c")
                change=change-(change5*5)
            
        if change>=1 and change<5:                  #change for 1c
            print(change, "x 1c")
            change=change-change 
        
        if change==0:
            flag=False            #end program s
        

