""" Change calculating POS program
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-14 """

# Initialize vars
cost = 0
paid = 0

cost = eval(input('Enter the cost (in cents):\n'))

def getchange(cost,paid):
    change = paid-cost
    receipt = 'Your change is:\n'
    # checks for the dollar place
    if change//100 != 0:
        receipt = receipt + str(change//100) + ' x $1\n'
        # removes the dollar place
        change = change%100
    # checks if there's any reamining change to be given
    if change != 0:
        # check how much of the remaining change can be given in 25c coins
        if change//25 != 0:
            receipt = receipt + str(change//25) + ' x 25c\n'
            # finds the remaining change
            change -= 25*(change//25)
        # check how much of the remaining change can be given in 10c coins
        if change//10 !=0:
            receipt = receipt + str(change//10) + ' x 10c\n'
            # finds the remaining change
            change -= 10*(change//10) 
        # check how much of the remaining change can be given in 5c coins
        if change//5 != 0:
            receipt = receipt + str(change//5) + ' x 5c\n'
            # finds the remaining change
            change -= 5*(change//5)
        # check how much of the remaining change can be given in 1c coins
        if change//1 != 0:
            receipt = receipt + str(change//1) + ' x 1c\n'   
    # Remove a trailing newline from the receipt
    receipt = receipt[:len(receipt)-1]
    return receipt

if cost != 0:
    # Prompt the user to keep adding money until the cost is met or exceeded
    while paid < cost:
        paid += eval(input('Deposit a coin or note (in cents):\n'))
    if paid-cost != 0:
        print(getchange(cost,paid))