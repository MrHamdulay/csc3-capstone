cost=eval(input("Enter the cost (in cents):\n"))
deposit=eval(input("Deposit a coin or note (in cents):\n"))

if deposit<cost:
    while deposit<cost:
        a=eval(input("Deposit a coin or note (in cents):\n"))
        deposit=deposit+a

if deposit>=cost:
    c=deposit-cost
    
    s=c//100
    t=(c%100)//25
    u=((c%100)%25)//10
    v=(((c%100)%25)%10)//5
    w=((((c%100)%25)%10)%5)
    
    print("Your change is:")
    
    if s>0:
        print(s,"x $1")
    
    if t>0:
        print(t,"x 25c")
    
    if u>0:
        print(u,"x 10c")
        
    if v>0:
        print(v,"x 5c")
        
    if w>0:
        print(w,"x 1c")
        
        
        