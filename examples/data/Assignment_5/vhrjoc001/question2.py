#jocelyn
#question 2
#making the costinfg for a vending machine
cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
change=0
if cost==0:
  print("")

else:
  deposit=eval(input("Deposit a coin or note (in cents):\n"))
  while cost>deposit:
    deposit2=eval(input("Deposit a coin or note (in cents):\n"))
    deposit+=deposit2  
  
#calculating required change  

if deposit>cost:
  change=deposit-cost
#breaking change into given money


if change!=0:
  print("Your change is:")
#using 1$

if change//100:
  print(change//100, "x $1")
  change%=100
  
# for 25c
if change//25:
  print(change//25, "x 25c")
  change%=25
  
# for 10$
if change//10:
  print(change//10, "x 10c")
  change%=10

#for 5c
if change//5:
  print(change//5, "x 5c")
  change%=5
  
#for 1c
if change//1:
  print(change//1, "x 1c")
  change%=1
   
  
    
