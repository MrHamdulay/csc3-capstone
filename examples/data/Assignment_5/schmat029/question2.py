#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     13-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

deposit = 0

cost = eval(input("Enter the cost (in cents): \n"))

while deposit < cost:
    deposit += eval(input("Deposit a coin or note (in cents): \n"))

rest = deposit - cost

if rest > 0:
    print("Your change is:")

    for coins in [100, 25, 10, 5, 1]:
        n = rest // coins
        if n == 0:
            continue
        if coins == 100:
            print(n, "x $1")
        else:
            print(n, " x ", coins, "c", sep="")
        rest -= coins * n