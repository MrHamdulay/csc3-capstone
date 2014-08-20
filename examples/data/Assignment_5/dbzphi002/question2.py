#Thembekile Dubazana
#Assignment 5:Q2
#dbzphi002

#change=1c, 5c, 10c, 25c, $1
cost=eval(input('Enter the cost (in cents):\n'))
deposit=0

#Loop for checking deposit
while deposit < cost:
    deposit+=eval(input('Deposit a coin or note (in cents):\n'))

#Calculate change
change = deposit - cost
if change != 0:
    print("Your change is:")
    while change > 0:
        if change//100 > 0:
            dig = str(change//100)
            change=change-((change//100)*100)
            print(dig,"x $1")
        elif change//25 > 0:
            dig2 = str(change//25)
            change=change-((change//25)*25)
            print(dig2,"x 25c")
        elif change//10 > 0:
            dig3 = str(change//10)
            change=change-((change//10)*10)
            print(dig3,"x 10c")
        elif change//5 > 0:
            dig4 = str(change//5)
            change=change-((change//5)*5)
            print(dig4,"x 5c")
        else:
            print(change,"x 1c")

        