# Program to simulate vending machine
# Nevarr Pillay - PLLNEV006
# 12 April 2014

def change(amount):
    change = [0,0,0,0,0]
    denom = ["$1","25c","10c","5c","1c"]
    while amount >= 100:
        change[0] += 1 
        amount -= 100
    while amount >= 25:
        change[1] += 1
        amount -= 25
    while amount >= 10:
        change[2] += 1
        amount -= 10
    while amount >= 5:
        change[3] += 1
        amount -= 5
    while amount > 0:
        change[4] += 1
        amount -= 1                    
    print("Your change is:")    
    for i in range(len(denom)):
        if change[i] > 0:
            print(change[i],"x",denom[i])

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    paid = 0
    if cost > 0:
        while paid < cost:
            dep = eval(input("Deposit a coin or note (in cents):\n"))
            paid += dep
        change2 = paid - cost
        if change2 > 0:
            change(change2)
    
main()    