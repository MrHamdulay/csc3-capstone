# calculate change in vending machine ($)
# bh
# 11 april 2014

cost = eval (input ("Enter the cost (in cents):\n"))

tender = 0
             
while tender < cost:
   tender += eval (input ("Deposit a coin or note (in cents):\n"))
               
change = tender - cost
if change>0:
   print ("Your change is:")

coin100 = change // 100
change -= coin100 * 100
coin25 = change // 25
change -= coin25 * 25
coin10 = change // 10
change -= coin10 * 10
coin5 = change // 5
change -= coin5 * 5
coin1 = change // 1
change -= coin1 * 1


if coin100 > 0:
   print (coin100, "x $1") 
if coin25 > 0:
   print (coin25, "x 25c") 
if coin10 > 0:
   print (coin10, "x 10c") 
if coin5 > 0:
   print (coin5, "x 5c") 
if coin1 > 0:
   print (coin1, "x 1c") 
 
   