#Ariel Rubin
#RBNARI001
#16 April 2014
#a program to simulate a cvending machine

#ask user to enter a value for cost
cost = eval (input ("Enter the cost (in cents):\n"))
#creating variables to be used later in the program
total = 0
count = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

#when cost has value of 0, a blank space is displayed
if cost == 0:
    print (" ")

#while loop repeatedly asks user to enter an amount 
#keeps adding amount to total variable
while total < cost:
    deposit = eval (input ("Deposit a coin or note (in cents):\n"))
    total = total + deposit

#when total amount is greater then cost, program displays values for change leftover 
if total > cost:
    print("Your change is:")
    newtotal = total - cost
#while loop counting how many times total has 100 value greater than cost
#100 is subtracted from total each time loop goes round
#if statement displays value for count to indicate how many $1 there are in the change left over
    while newtotal >= 100:
        count = count + 1
        newtotal = newtotal - 100
    if count >= 1:
        print(count,"x $1",sep=" ")
#while loop counting how many times total has 25 value greater than cost
#25 is subtracted from total each time loop goes round
#if statement displays value for count to indicate how many 25c there are in the change left over
    while newtotal >= 25:
        count2 = count2 + 1
        newtotal = newtotal - 25
    if count2 >= 1:
        print(count2,"x 25c",sep=" ") 
#while loop counting how many times total has 10 value greater than cost
#10 is subtracted from total each time loop goes round
#if statement displays value for count to indicate how many 10c there are in the change left over
    while newtotal >= 10:
        count3 = count3 + 1
        newtotal = newtotal - 10
    if count3 >= 1:
        print(count3,"x 10c",sep=" ") 
#while loop counting how many times total has 5 value greater than cost
#5 is subtracted from total each time loop goes round
#if statement displays value for count to indicate how many 5c there are in the change left over
    while newtotal >= 5:
        count4 = count4 + 1
        newtotal = newtotal - 5
    if count4 >= 1:
        print(count4,"x 5c",sep=" ") 
#while loop counting how many times total has 1 value greater than cost
#1 is subtracted from total each time loop goes round
#if statement displays value for count to indicate how many 1c there are in the change left over
    while newtotal >= 1:
        count5 = count5 + 1
        newtotal = newtotal - 1
    if count5 >= 1:
        print(count5,"x 1c",sep=" ") 
#when value of cost equals vale of total, a blank space is displayed
elif total == cost:
    print(" ")



        