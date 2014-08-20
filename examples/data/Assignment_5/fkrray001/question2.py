# Author : Rayaan Fakier FKRRAY001
# Date : 14 - 04 - 2014
# Program that simulates vending machine

def main():
    cost = int(input("Enter the cost (in cents):\n"))
    payment = 0 # Initializes and starts payment at 0
    while payment < cost: # Loops until pays atleast cost value
        deposit = int(input("Deposit a coin or note (in cents):\n"))
        payment += deposit
    change = payment - cost
    if change == 0: # Ends if change is 'initially' 0
        return
    print("Your change is:")
    # Initialize change amounts
    dollars = 0
    quarters = 0
    tencent = 0
    fivecent = 0
    onecent = 0
    # While loops to break down change into constituents by decreasing it per 
    # "change level'
    while change > 99:
        dollars += 1
        change -= 100
    while change > 24:
        quarters += 1
        change -= 25
    while change > 9:
        tencent += 1
        change -= 10
    while change > 4:
        fivecent += 1
        change -= 5
    onecent += change # onecent is the leftover of the change
    # If statements to remove the "0" of a 'change level'
    if dollars:
        print(dollars, "x $1")
    if quarters > 0:
        print(quarters, "x 25c")
    if tencent:
        print(tencent, "x 10c")
    if fivecent:
        print(fivecent, "x 5c")
    if onecent:
        print(onecent, "x 1c")
        
        
main()