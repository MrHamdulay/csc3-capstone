'''this programm calculates change based on the amount paid
Nxumalo Goodman
14 April 2014'''

def change():
    cost = eval(input("Enter the cost (in cents):\n"))
    Deposit = 0
    while Deposit < cost:
        Deposite = eval(input("Deposit a coin or note (in cents):\n"))
        Deposit += Deposite
        
    if Deposit > cost:    
        change = Deposit - cost
        remainder = change % 100
        remainde = remainder % 25
        remaind = remainde % 10
        remain = remaind % 5 
        print("Your change is:")
        if change >= 100:
            factor = int(change / 100)
            print(factor ,"x $1")
        if remainder >= 25:
            facto = int(remainder / 25)
            print(facto ,"x 25c")
        if remainde >= 10:
            fact = int(remainde / 10)
            print(fact ,"x 10c")
        if remaind >= 5:
            fac = int(remaind / 5)
            print(fac ,"x 5c")
        if remain >= 1:
            fa = int(remain / 1)
            print(fa ,"x 1c")
    
change()