#Vending machine program
#Author: Litha Maqungo
# 16 April 2014

print("Enter the cost:") #for the user to enter the cost of the item
cost = int(input())
amount = 0
while amount < cost: #so that it loops until the cost is covered
    print("Deposit a coin or note (in cents):")
    deposit = int(input())
    amount = amount + deposit #putting the deposit into the amount
change = amount - cost
onedollars = round(change//100)
twentyfivecents = round(((change/100)-onedollars)//0.25)
tencents = round((change/100-(onedollars + twentyfivecents))//0.10)
fivecents = round((change-(onedollars*100) - (twentyfivecents*25) - (tencents*10))//5)
onecents = round((change/100-(onedollars + twentyfivecents + tencents + fivecents))//0.01)
print("Your change is:" ) #ensuring that only if it's positive it outputs the coin
if onedollars > 0:
    print( onedollars ,"x $1")
if twentyfivecents > 0:
    print( twentyfivecents, "x 25c")
if tencents > 0:
    print(tencents,"x 10c")
if fivecents > 0:
    print (fivecents,"x 5c")
if onecents > 0:
    print (onecents, "x 1c")
    

