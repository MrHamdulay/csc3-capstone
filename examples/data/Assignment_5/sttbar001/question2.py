money =0
cost =0
cost = eval(input("Enter the cost (in cents): \n"))
while money < cost:
    money = (eval(input("Deposit a coin or note (in cents): \n")))+money
    
change = money-cost 
if change!= 0:
    print("Your change is:")

doll1 = int(change/100)
if doll1 >0:
    print(str(doll1)+" x $1")
change = change - (doll1*100)

doll2 = int(change/25)
if doll2 >0:
    print(str(doll2)+" x 25c")
change = change - (doll2*25)

doll3 = int(change/10)
if doll3 >0:
    print(str(doll3)+" x 10c")
change = change - (doll3*10)

doll4 = int(change/5)
if doll4 >0:
    print(str(doll4)+" x 5c")
change = change - (doll4*5)

if change >0:
    print(str(change)+ " x1c")