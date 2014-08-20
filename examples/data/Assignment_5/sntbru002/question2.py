def sim():
    cost=int(input("Enter the cost (in cents):\n"))
    amt=int(input("Deposit a coin or note (in cents):\n"))
    while amt<cost:
        x=int(input("Deposit a coin or note (in cents):\n"))
        amt=amt+x
    change=amt-cost
    if change!=0:
        print("Your change is:")
    r=change//100
    c=change%100
    f=r//5
    if f!=0:
        print(f,"x","R5")
    t=(r%5)//2
    if t!=0:
        print(t,"x","R2")
    o=((r%5)%2)//1
    if o!=0:
        print(o,"x","R1")
    fc=c//50
    if fc!=0:
        print(fc,"x","50c")
    twc=(c%50)//20
    if twc!=0:
        print(twc,"x","20c")
    tenc=((c%50)%20)//10
    if tenc!=0:
        print(tenc,"x","10c")
    fcent=(((c%50)%20)%10)//5
    if fcent!=0:
        print(fcent,"x","5c")
        
        
sim()
        
    