cost = eval(input("Enter the cost (in cents):\n"))

payed = 0

while payed < cost:
    payed+= eval(input("Deposit a coin or note (in cents):\n"))
    
ichange = payed - cost    
change = payed - cost
dollars = int(change/100)
change -= dollars*100
quarters = int(change/25)
change -= quarters*25
dimes = int(change/10)
change -= dimes*10
nickels = int(change/5)
change -= nickels*5
cents = int(change)


if payed > 0 and ichange > 0:
    print ("Your change is:")
if dollars != 0:
    print (dollars,"x $1")
if quarters != 0:
    print (quarters,"x 25c")
if dimes != 0:
    print (dimes,"x 10c")
if nickels != 0:
    print (nickels,"x 5c")
if cents != 0:
    print (cents,"x 1c")