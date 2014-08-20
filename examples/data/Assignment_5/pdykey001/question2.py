"""Vending Machine
Keyoolin Padayachee
16 April 2014
"""
cost=eval(input("Enter the cost (in cents):\n"))
paid=0
while paid<cost:
    #work out how much is paid till it is more than the cost amount
    paid=paid+eval(input("Deposit a coin or note (in cents):\n")) 
change=paid-cost
#working out the change amount in terms of coins
dollar=change//100
quarter=(change%100)//25
ten=((change%100)-(quarter*25))//10
five=((change%100)-(quarter*25)-(ten*10))//5
cent=((change%100)-(quarter*25)-(ten*10)-(five*5))
if change != 0:print("Your change is:")
if dollar != 0:print(dollar,"x $1")
if quarter != 0:print(quarter,"x 25c")
if ten != 0:print(ten,"x 10c")
if five != 0:print(five,"x 5c")
if cent != 0:print(cent,"x 1c")