# A program to simulate a vending machine and calculate change.
# Retselisitsoe Monyake
# 16 April 2014

cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
while deposit <cost:
    deposit2=eval(input("Deposit a coin or note (in cents):\n"))
    deposit+=deposit2
    if deposit>=cost:
        break
#calculating the change
change=int(deposit-cost)
dollars=change//100
change_remaining=change%100
twenty_five=change_remaining//25
change_remaining2=change_remaining%25
ten=change_remaining2//10
change_remaining3=change_remaining2%10
five=change_remaining3//5
change_remaining4=five%5
if change!=0:
    print("Your change is:")
if dollars!=0:
    print(dollars,"x $1")
if twenty_five!=0:
    print(twenty_five,"x 25c")
if ten!=0:
    print(ten,"x 10c")
if five!=0:
    print(five,"x 5c")
if change_remaining4!=0:
    print(change_remaining4,"x 1c")
    

 

    
