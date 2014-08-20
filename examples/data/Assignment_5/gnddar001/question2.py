#Q2ASS5
#14.04.14

cost = eval(input("Enter the cost (in cents):\n"))

deposit = 0


while deposit < cost:
    deposit += eval(input("Deposit a coin or note (in cents):\n"))
    
change = deposit - cost

if change == 0:
    print("")
    
else:
    a = change//100
    if a>0:
        change -= (a*100)
    
    b = change//25
    if b>0:
        change -= (b*25)
    
    c = change//10
    if c>0:
        change -= (c*10)
    
    d = change//5
    if d>0:
        change -= (d*5)
    
    e = change//1
    
    print("Your change is:")
    
    if a>0:
        print(a, "x $1")
        
    if b>0:
        print(b, "x 25c")
        
    if c>0:
        print(c, "x 10c")
        
    if d>0:
        print(d, "x 5c")
        
    if e>0:
        print(e, "x 1c")
    
    
    
    
