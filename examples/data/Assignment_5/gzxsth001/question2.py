cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
while deposit<cost:
    depo=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=depo+deposit
if deposit!=cost:
    change=deposit-cost
    print("Your change is:")
    dollar=change//100
    if dollar!=0:
        print(dollar,"x $1")
    remainder=change%100
    if remainder!=0:
        cents=remainder//25
        if cents!=0:
            print(cents,"x 25c")
    remainder=remainder%25
    if remainder!=0:
        cent=remainder//10
        if cent!=0:
            print(cent,"x 10c")
    remainder=remainder%10
    if remainder!=0:
        bronze=remainder//5
        if bronze!=0:
            print(bronze,"x 5c")
    remainder=remainder%5
    if remainder!=0:
        pennies=remainder//1
        if pennies!=0:
            print(pennies,"x 1c")
    


                    
    