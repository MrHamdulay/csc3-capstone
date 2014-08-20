#Kieran Reilly, RLLKIE001
#Assignment5, question2
#Change Calculater(dollars)
#13/04/14

cost = 0
payed = 0
change = 0

dollarCount = 0
quarterCount = 0
dimeCount = 0
nickleCount = 0
pennyCount = 0


cost = int(eval(input("Enter the cost (in cents): \n")))

while payed < cost:
    payed = payed + int(eval(input("Deposit a coin or note (in cents): \n")))


change = int(payed - cost)

if change != 0:
    print("Your change is: ")

while change != 0 :
    if(change >= 100):
        change = change - 100
        dollarCount = dollarCount +1
    elif(change >= 25 and change < 100):
        change = change - 25
        quarterCount = quarterCount +1
    elif(change >=10 and change < 25):
        change = change - 10
        dimeCount = dimeCount +1
    elif(change >= 5 and change < 10):
        change = change - 5
        nickleCount = nickleCount +1
    elif(change >=1 and change <5):
        change = change -1
        pennyCount = pennyCount +1
    
if dollarCount > 0:
    print(str(dollarCount) + " x $1")
if quarterCount > 0:
    print(str(quarterCount) + " x 25c")
if dimeCount > 0 :
    print(str(dimeCount) + " x 10c")
if nickleCount > 0:
    print(str(nickleCount) + " x 5c")
if pennyCount > 0:
    print(str(pennyCount) + " x 1c")


