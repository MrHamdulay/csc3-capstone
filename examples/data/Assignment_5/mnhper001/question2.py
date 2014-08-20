
#Author:Percival Munhuwaani
#Date:16/04/2014
#Program:A program that simulates a vending machine
def main():
    cost=eval(input("Enter the cost (in cents):\n")) #The price of the item sold
    deposit=0 #When no money has been entered yet
    while deposit<cost:
        amount_dep=eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=amount_dep #Increasing the amount of the money entered
    change=deposit-cost
    new_change=change
    if(change>0): #Printing only when there is change
        print("Your change is:")
        if change>=100:
            print(change//100, "x $1")
            new_change=change%100
        if new_change>=25:
            print(new_change//25,"x 25c")
            new_change=new_change%25
        if new_change>=10:
            print(new_change//10,"x 10c")
            new_change=new_change%10
        if new_change>=5:
            print(new_change//5,"x 5")
            new_change=new_change%5
        if new_change!=0:
            print(new_change,"x 1c")
main()
        