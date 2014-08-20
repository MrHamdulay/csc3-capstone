Price = eval(input("Enter the cost (in cents):\n"))
if Price == 0:
    print("")
else:    
    User = eval(input("Deposit a coin or note (in cents):\n"))
    while Price > User:
        User += eval(input("Deposit a coin or note (in cents):\n"))
    D1 = 0
    C25 = 0
    C10 = 0
    C5 = 0
    C1 = 0
    Total = User-Price
    Total1 = User-Price
    while Total > 0:
        if (Total >= 100):
            Total -= 100
            D1 = D1 + 1
        elif (Total >= 25):
            Total -= 25
            C25 = C25 + 1    
        elif (Total >= 10):
            Total -= 10
            C10 = C10 + 1
        elif (Total >= 5):
            Total -= 5
            C5 = C5 + 1    
        elif (Total >= 1):
            Total -= 10
            C1 = C1 + 1
    if Total1 !=0:            
        print("Your change is:")
        if (D1 > 0):
            print (D1,"x","$1")
        if (C25 > 0):
            print (C25,"x","25c")
        if (C10 > 0):
            print (C10,"x","10c")
        if (C5 > 0):
            print (C5,"x","5c")
        if (C1 > 0):
            print (C1,"x","1c")

                                         