#VRMNIC005
#assignment 5, question 2

def vending():
    """calculates the amount of change given by a vending machine"""
    cost = int(input("Enter the cost (in cents): \n"))
    deposit = 0
    while deposit < cost:
        deposit += int(input("Deposit a coin or note (in cents): \n"))

    change = deposit - cost
    if change > 0:
        print("Your change is: ")
        for coin in (100, 25, 10, 5, 1):
            result = change // coin  #integer divides to give the number of coins
            if result != 0:
                if coin == 100:
                    print(result, "x $1")

                else:
                    print(result, " x ", coin, "c", sep="")
            change %= coin

vending()
