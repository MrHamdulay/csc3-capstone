"""CSC1015F Assignment 5 Question 2
Xola Matlanyane MTLXOL002
17 April 2014"""

#asking user for cost
cost=eval(input("Enter the cost (in cents):\n"))

#asking for deposit
dep=0
while dep < cost:
    dep2=eval(input("Deposit a coin or note (in cents):\n"))
    dep+=dep2
    
change=dep-cost     #calculating change

#calculating change in terms of denoninations
dollars = change//100
rem1 = change%100
quarters = rem1//25
rem2 = rem1%25
tens = rem2//10
rem3 = rem2%10
fives = rem3//5
rem4 = rem3%5
ones = rem4

#printing out change according to denomination representation
if change>0:
    print("Your change is:")
if dollars>=1:
    print(dollars,"x $1")
if quarters>=1:
    print(quarters,"x 25c")
if tens>=1:
    print(tens,"x 10c")
if fives>=1:
    print(fives,"x 5c")
if ones>=1:
    print(ones,"x 1c")

