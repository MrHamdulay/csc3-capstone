#deducting from balance in deniminations
#wayne de jager
#14 april 2014

balance=0
cost=eval(input("Enter the cost (in cents):\n"))

#records current balance after each payment
while cost>balance:
    paid=eval(input("Deposit a coin or note (in cents):\n"))
    balance=balance+paid
change=balance-cost

#calculates change
dollars=change//100
twentyfivec=(change-(dollars*100))//25
tenc=(change-(dollars*100)-(twentyfivec*25))//10
fivec=(change-(dollars*100)-(twentyfivec*25)-(tenc*10))//5
onec=(change-(dollars*100)-(twentyfivec*25)-(tenc*10)-(fivec*5))//1

#display change deniminations
if change!=0:
    print("Your change is:")
if dollars!=0:
    print(dollars,"x $1")
if twentyfivec!=0:
    print(twentyfivec,"x 25c")
if tenc!=0:
    print(tenc,"x 10c")
if fivec!=0:
    print(fivec,"x 5c")
if onec!=0:
    print(onec,"x 1c")