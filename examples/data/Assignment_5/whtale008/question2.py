"""mymath
alexander whiting
18 april 2014"""

cost = int(input("Enter the cost (in cents):\n"))
deposit = 0
while deposit < cost:
    deposit = deposit + int(input("Deposit a coin or note (in cents):"))
    print()
change = deposit -cost
if change !=0:
    print("Your change is:")
    for i in (100,25,10,5,1):
        f = change//i
        change = change - i*f
        if f!=0:
            if i == 1:
                print(str(f)+" x 1c")
            elif i == 5:
                print(str(f)+" x 5c")
            elif i == 10:
                print(str(f)+" x 10c")
            elif i == 25:
                print(str(f)+" x 25c")
            elif i == 100:
                print(str(f)+" x $1")            
            