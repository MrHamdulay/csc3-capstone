"""Dumisani Ngwenza
NGWDUM005
03/04/2014
Assignment 5 question 2"""

#get cost from user
cost = eval (input("Enter the cost (in cents):\n"))
money = 0
difference =0
#Calculate change
if cost != 0:
    money = eval (input("Deposit a coin or note (in cents):\n"))
    difference = money - cost
    while difference < 0:
        x = eval (input("Deposit a coin or note (in cents):\n"))
        money += x
        difference = money - cost
        
if money != cost: 
    print ("Your change is:")
    
# calculates the $1 change
if difference//100 !=0:
    coin = difference//100
    difference -= coin*100
    if coin > 0:
        print (coin, 'x', '$1', sep =" ")
        
#calculates the 25c change        
if difference >= 25:
    coin = difference//25
    if coin >0:
        print (coin, 'x', '25c', sep = " ")
    difference -= coin*25
    
#calculates the 10c change    
if difference >= 10:
    coin = difference//10
    if coin >0:
        print (coin, 'x', '10c', sep =' ')
    difference -= coin*10

#calculates the 5c change    
if difference >= 5:
    coin = difference//5
    if coin > 0:
        print (coin, 'x', '5c', sep  = ' ')
else:#calculates the 1c change
    coin = difference
    if coin > 0:
        print (coin, 'x', '1c', sep ='')



