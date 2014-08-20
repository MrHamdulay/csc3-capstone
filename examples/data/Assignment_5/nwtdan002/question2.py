"""Simulation of change given by a vending machine
By Daniel Newton
13/04/14"""

tot=eval(input("Enter the cost (in cents):\n"))

if tot!=0:  #Ensuring the amount you enter is greater than 0 (Otherwise nothing further required)
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    
    while (tot-deposit)>0:  #Prompts the user to enter amounts until the amount payed is >= the amount owed.
        deposit2=eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=deposit2
    change=abs(deposit-tot)
    if change!=0:
        print("Your change is:")
    
    #Initially all amount of change are 0.
    dollars=0
    cents25=0
    cents10=0
    cents5=0
    cents1=0
    
    #Evaluating the remaining change.
    if change>=100:     #How much change can be given in dollars...
        dollars=change//100
        print(dollars,"x $1")
    change-=(dollars*100)
    if change>=25:      #How much remaining change can be given as 25c...
        cents25=change//25
        print(cents25,"x 25c")
    change-=(cents25*25)
    if change>=10:      #And so on to 10c...
        cents10=change//10
        print(cents10,"x 10c")
    change-=(cents10*10)
    if change>=5:       #5c...
        cents5=change//5
        print(cents5,"x 5c")
    change-=(cents5*5)
    if change>=1:       #1c...
        cents1=change//1
        print(cents1,"x 1c")