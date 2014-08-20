#Alexi Kalamoudacos
#Assignment 5
#Question 2
#17 April 2014
 
 
#Ask user how much product is
cost = eval(input("Enter the cost (in cents):\n"))
money = 0

while money < cost:
   y = eval(input("Deposit a coin or note (in cents):\n"))
   money = money + y
  
change = money - cost
if change != 0:
   print('Your change is:')
#Check to see if change is more than $1
countdollar = 0
while change >= 100:
   change = change - 100
   countdollar = countdollar + 1
#Check to see if change is more than 25c
countquarter = 0
while change >= 25:
   change = change - 25
   countquarter = countquarter + 1
  
#Check to see if change is more than 10c  
  
countten = 0
while change >= 10:
   change = change -10
   countten = countten + 1
  
#Check to see if change is more than 5c  
  
countfive = 0
while change >= 5:
   change = change -5
   countfive = countfive + 1
  
#Check to see if change is more than 1c  
  
countone = 0
while change >= 1:
   change = change -1
   countone = countone + 1
  
  
if countdollar > 0  or  (countquarter > 0) or (countten > 0) or (countfive > 0) or (countone > 0):
   if countdollar > 0:
      print(countdollar, "x $1")
   if countquarter > 0:
      print(countquarter, "x 25c")
   if countten > 0:
      print(countten, "x 10c")
   if countfive > 0:
      print(countfive, "x 5c")
   if countone > 0:
      print(countone, "x 1c")