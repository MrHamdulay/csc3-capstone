#Phumelele Ndimande
#Assignment 5

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    amount=0
    change=0
    while amount<cost:
        amount+= eval(input("Deposit a coin or note (in cents):\n"))
     #calculate change   
    change = amount - cost
    
    #seperate the change according to available denominations
    if change != 0:
        print("Your change is:")
        if change//100 != 0:
            print((change//100), "x $1")
            change = change - ((change//100) * 100)
        if change//25 !=0:
            print((change//25), "x 25c")
            change= change - ((change//25)* 25)
        if change//10 !=0:
            print((change//10), "x 10c")
            change= change - ((change//10)*10)
        if change//5 !=0:
            print((change//5), "x 5c")
            change = change -((change//5)*5)
        if change !=0:
            print(change, "x 1c")

main()
