'''Jason Pietersen'''
#Program used to calculate the change from a transaction

amount = eval(input("Enter the cost (in cents):\n"))

while amount>0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    amount -= deposit
    
if amount!=0:    
    print("Your change is:")
    
    dollar = (amount*-1)//100
    quarters = ((amount*-1)%100)//25
    cents10 = (((amount*-1)%100)%25)//10
    cents5 = ((((amount*-1)%100)%25)%10)//5
    cents1 = (((((amount*-1)%100)%25)%10)%5)
    
    change = [dollar,quarters,cents10,cents5,cents1]
    symbol = ["$1","25c","10c","5c","1c"]
    
    j=0
    for i in change:
        if i == 0:
            j += 1
            continue
        else:
            print(str(i)+" x "+symbol[j])
            j += 1