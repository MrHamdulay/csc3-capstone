'''A vending machine change system simulator'''
### Tashiv Sewpersad
### Assignment 5 - Question 2
### 14 - 04 - 2014

## Constants
coins = [100,25,10,5,1] # in cents
sCoins = ["$1","25c","10c","5c","1c"] # corresponding string

## Live code
iDeposit = 0
iCost = eval(input("Enter the cost (in cents):\n"))
while iDeposit < iCost:
  iDeposit += eval(input("Deposit a coin or note (in cents):\n"))
sOutput = ""
iChange = iDeposit - iCost
for i in range(5):
  amount = iChange//coins[i]
  if amount > 0:
    sOutput += str(amount) + " x " + sCoins[i] + "\n" #Builds output string
    iChange -= amount*coins[i]
if sOutput != "":
  print("Your change is:")
  print(sOutput,end="")
 