#Question 2: Vending Machine Simulator
#Jennifer Yuan
#13 April 2014

Cost = eval(input("Enter the cost (in cents):\n"))

if Cost == 0: #if Cost=0, do not ask to deposit money
    print("")
if Cost>0: #only ask to deposit money of there is a cost
    Deposit = eval(input("Deposit a coin or note (in cents):\n"))
    while Deposit < Cost: #if more money still needs to be put in
        Added = eval(input("Deposit a coin or note (in cents):\n"))
        Deposit = Deposit + Added #asks for more money until enough money put in to cover Cost
    if Cost==Deposit: #if no change is needed
        print("")
    else:
        change = Deposit - Cost #calculating change
        dollars = change//100 #calcuting how much of each "coin" is needed
        twentyfive = (change - (dollars*100))//25 #taking remainder to work out how much needed of "smaller" coin
        ten= (change - (dollars*100) - (twentyfive*25))//10
        five =(change - (dollars*100) - (twentyfive*25) - (ten*10))//5
        ones = change - (dollars*100) - (twentyfive*25) - (ten*10) - (five*5)
        print("Your change is:")
        if dollars>0: #does not print if coin is not needed for change
            print(dollars ,"x $1")
        if twentyfive>0:
            print(twentyfive, "x 25c")
        if ten>0:
            print(ten, "x 10c")
        if five>0:
            print(five, "x 5c")
        if ones>0:
            print(ones, "x 1c")