#Assume that all change is given in coins only and coins come in the following denominations: 1c, 5c, 10c, 25c, $1

#change giving program
#Tayla Radmore
#15 April 2014

#get the cost
cost=eval(input("Enter the cost (in cents):\n"))
total=0

# add deposits
while total<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n")) 
    total+=deposit
    
total_change=total-cost
if total_change != 0:
    dollars=total_change//100
    if dollars != 0:
        x=str(dollars)
        final_dollars=x+" x $1 \n"
    else: final_dollars=""
    total_change= total_change-(dollars*100)

    twenty_five_cents=total_change//25
    if twenty_five_cents != 0:
        y=str(twenty_five_cents)
        final_25_cents=y+" x 25c \n"
    else: final_25_cents=""
    total_change= total_change-(twenty_five_cents*25)

    ten_cents= total_change//10
    if ten_cents !=0:
        z=str(ten_cents)
        final_10_cents=z+" x 10c \n"
    else: final_10_cents=""
    total_change=total_change-(ten_cents*10)

    five_cents=total_change//5
    if five_cents !=0:
        a=str(five_cents)
        final_5_cents=a+" x 5c \n"
    else: final_5_cents=""
    




    print("Your change is:\n",final_dollars,final_25_cents,final_10_cents,final_5_cents,sep="")

