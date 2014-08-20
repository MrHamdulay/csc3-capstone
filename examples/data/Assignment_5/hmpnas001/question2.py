def vending_machine():
    cost=eval(input("Enter the cost (in cents):\n"))
    deposit=0
    while deposit<cost:
        message=eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=message
        if deposit >= cost:
            break
    #change
    change=deposit-cost
    a=change//100
    b=(change%100)//25
    c=((change%100)%25)//10
    d=(((change%100)%25)%10)//5
    e=((((change%100)%25)%10)%5)//1
    
    if a!=0 or b!=0 or c!=0 or d!=0 or e!=0:
        print("Your change is:")
    if a!=0:
        print(a,"x $1")
    if b!=0:
        print(b,"x 25c")
    if c!=0:
        print(c,"x 10c")
    if d!=0: 
        print(d,"x 5c")
    if e!=0:
        print(e,"x 1c")
        
vending_machine()        
        
    
        
    