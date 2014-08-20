"""A program to simulate a vending machine
Author: Barnett Msiska
Date: 14/04/2014"""

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    payment = 0
    if cost == 0:
        pass
    else:
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        payment += deposit
        while payment < cost:
            deposit = eval(input("Deposit a coin or note (in cents):\n"))
            payment += deposit 
        change = payment - cost
        remainder = change
        if change:
            print("Your change is:")
            if change//100:
                print(change//100, 'x', '$1')
                remainder = change%100
            if remainder//25:
                print(remainder//25, 'x', '25c')
                remainder = remainder%25
            if remainder//10:
                print(remainder//10, 'x', '10c')
                remainder = remainder%10
            if remainder//5:
                print(remainder//5, 'x', '5c')
                remainder = remainder%5
            if remainder:
                print(remainder, 'x', '1c')
main()