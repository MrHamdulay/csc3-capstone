#Assignment 5
#Question 2
#Barry Su
#15 April 2014

#initiate the values for variables
cost = eval(input("Enter the cost (in cents):\n"))
deposit = 0
dollar = 0
twenty_5 = 0
tens = 0
fives = 0
ones = 0

#create a while-loop to count deposits added
while deposit < cost:
    x = eval(input("Deposit a coin or note (in cents):\n"))
    deposit = deposit + x
 
change = deposit - cost

if change > 0:
    print("Your change is:") 

#determine the change in terms of how many of each coin returned      
if change//100 >= 1:
    dollar = change//100
    change = change - dollar*100
if change//25 >=1:
    twenty_5 = change//25
    change = change - twenty_5*25
if change//10 >= 1:
    tens = change//10
    change = change - tens*10
if change//5 >=1:
    fives = change//5
    change = change - fives*5
if change//1 >=1:
    ones = change//1
    change = change - ones*1

if dollar >= 1:
    print(dollar, "x", "$1")
if twenty_5 >= 1:
    print(twenty_5, "x", "25c")
if tens >= 1:
    print(tens, "x", "10c")   
if fives >= 1:
    print(fives, "x", "5c")
if ones >= 1:
    print(ones, "x", "1c")
    