"""
A program to simulate a vending machine and calculate change based on the 
amount paid.
Jayan Smart
17 April 2014
"""


def main():
    #Prompt user for cost:
    cost = eval(input("Enter the cost (in cents):\n"))
    #Prompt user for payment:
    paid = 0
    while paid<cost:
        money = eval(input("Deposit a coin or note (in cents):\n"))
        paid+=money

    #Calculate change to be given:
    change = paid - cost
    if change == 0:
        print()
    else:
        dollar, change=(change-change%100)//100, change%100
        c25, change=(change-change%25)//25, change%25
        c10, change=(change-change%10)//10, change%10
        c5, change=(change-change%5)//5, change%5
        c1, change=(change-change%1)//1, change%1

        #Print the values for respective denominators of change:
        print("Your change is:")
        if dollar>0:
            print(dollar, "x $1")
        if c25>0:
            print(c25, "x 25c")
        if c10>0:
            print(c10, "x 10c")
        if c5>0:
            print(c5, "x 5c")
        if c1>0:
            print(c1, "x 1c")

main()
