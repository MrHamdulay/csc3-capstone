'''Vending Machine change given
Michael Sanne
15/04/2014'''

#Input output
deposit = 0
cost = eval (input ("Enter the cost (in cents):\n"))
#Input till deposit is sufficient
while deposit < cost:
    deposit += eval (input ("Deposit a coin or note (in cents):\n"))
    
#Determine amount of change that has to be given
change = deposit - cost
if change > 0:
    print ("Your change is:")

rand = 100
quater = 25
tens = 10
fiver = 5
cent = 1

rand = change // rand
change -= (rand*100)
quater = change // quater
change -= (quater*25)
tens = change // tens
change -= (tens*10)
fiver = change // fiver
change -= (fiver*5)
cent = change // cent

#Return amount of change if change exists
if (rand != 0):
    print (rand , "x $1")
if (quater != 0):
    print (quater , "x 25c")
if (tens != 0):
    print (tens , "x 10c")
if (fiver != 0):
    print (fiver , "x 5c")
if (cent != 0):
    print (cent , "x 1c")