"""Vending machine: to pay and receive change from a machine
Assignment 5
Nandani Birjanund
16/04/14"""
#Asks user for the cost of the item
x = eval(input("Enter the cost (in cents):\n"))
money = 0
while money < x:
   y = eval(input("Deposit a coin or note (in cents):\n")) #when the money paid is less than the cost of the item
   money = money + y #money given is now equal to the initial money plus the amount deposited
   change = money - x

if change != 0: #when change is not zero (cost is not equal to the deposit)
   print('Your change is:')

#Check if the change is > $1
countdollar = 0 
while change >= 100: #to get to change amount in dollars first
   change = change - 100
   countdollar = countdollar + 1

#Check if the change is > 25c
countquarter = 0          #for 50c coin
while change >= 25:
   change = change - 25
   countquarter = countquarter + 1
   
#Check if the change is > 10c      
countten = 0              #for 25c coin
while change >= 10:
   change = change -10
   countten = countten + 1
   
#Check if the change is > 5c      
countfive = 0
while change >= 5:           #for 10c coin
   change = change -5
   countfive = countfive + 1
   
#Check if the change is > 1c     
countone = 0          #for 5c coin
while change >= 1:
   change = change -1
   countone = countone + 1
      
if countdollar > 0  or  (countquarter > 0) or (countten > 0) or (countfive > 0) or (countone > 0):
   if countdollar > 0:
      print(countdollar, "x $1") #gives $1 denmoination
   if countquarter > 0:
      print(countquarter, "x 25c") #gives 25c denmoination
   if countten > 0:
      print(countten, "x 10c") #gives 10c denmoination
   if countfive > 0:
      print(countfive, "x 5c") #gives 5c denmoination
   if countone > 0:
      print(countone, "x 1c") #gives 1c denmoination