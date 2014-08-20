#Write a program to simulate a vending machine and calculate change based on the amount paid. Given the cost, the user should first be prompted to add more money until the cost is met/exceeded by the payment.

#Assume that all change is given in coins only and coins come in the following denominations: 1c, 5c, 10c, 25c, $


cost=eval(input("Enter the cost (in cents): \n"))
balance=0
while balance<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    balance+=deposit

if balance - cost != 0:
    balance-=cost
    cents=balance%100
    quarter=0
    tens=0
    fives=0 
    ones=0
    if cents//25>0:
        quarter=cents//25
        cents=cents%25
    if cents//10>0:
        tens=cents//10
        cents=cents%10
    if cents//5>0:
        fives=cents//5
        cents=cents%5
    if cents>0:
        ones=cents
        cents=0

                    
    dollars=balance//100
    print("Your change is:")
    if dollars>0:
        print(dollars," x $1",sep="")
    if quarter>0:
        print(quarter,"x 25c")
    if tens>0:
        print(tens,"x 10c")
    if fives>0:
        print(fives,"x 5c")
    if ones>0:
        print(ones,"x 1c")

    