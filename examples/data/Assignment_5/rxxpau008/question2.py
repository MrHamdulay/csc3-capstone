#Description: Calculates the change from a payment
#Name: Paul Roux - RXXPAU008
#Date: 15 April 2014

cost = int(input("Enter the cost (in cents):\n"))
pay = 0
while cost>pay:
    pay = pay+int(input("Deposit a coin or note (in cents):\n"))
change = pay-cost
if change !=0: print("Your change is: ")
while change:#While change has a value, the change required will be calculated from the largest denomination
    if (change//100)!=0:
        print(change//100,"x $1")
        change = change-((change//100)*100)
    elif (change//25)!=0:
        print(change//25,"x 25c")
        change = change-((change//25)*25)
    elif (change//10)!=0:
        print(change//10,"x 10c")
        change = change-((change//10)*10)
    elif (change//5)!=0:
            print(change//5,"x 5c")
            change = change-((change//5)*5)

