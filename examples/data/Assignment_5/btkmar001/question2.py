# Assignment 5, Question 2 
# A program which simulates a change counter based on amount paid
# Martin Batek
# 14 April 2014

deposit = 0
num100c = 0
num25c = 0
num10c = 0
num5c = 0
num1c = 0
cost = eval(input("Enter the cost (in cents):\n"))

while deposit < cost:
    deposit += eval(input("Deposit a coin or note (in cents):\n"))
    
while (deposit-cost) >= 100:
    num100c += 1
    deposit -= 100
    
while (deposit-cost) >= 25:
    num25c += 1
    deposit -= 25
    
while (deposit-cost) >= 10:
    num10c += 1
    deposit -= 10
    
while (deposit-cost) >= 5:
    num5c += 1
    deposit -= 5
    
while (deposit-cost) >= 1:
    num1c += 1
    deposit -= 1
    
if num100c != 0 or num25c != 0 or num10c != 0 or num5c != 0 or num1c != 0:
    print("Your change is:")

if num100c > 0:
    print(num100c,"x $1")
    
if num25c > 0:
    print(num25c,"x 25c")

if num10c > 0:
    print(num10c,"x 10c")
    
if num5c > 0:
    print(num5c,"x 5c")
    
if num1c > 0:
    print(num1c,"x 1c")