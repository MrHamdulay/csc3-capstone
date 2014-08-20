cost = int(input("Enter the cost (in cents): \n"))
deposited = 0 
while deposited < cost:
    deposited+= int(input("Deposit a coin or note (in cents):\n"))
change = deposited-cost
manipulate = str(change)
ones = int(manipulate[-1])%5
tens = (int(manipulate[-2:])%25)//10
twfvs =(int(manipulate[-2:]))//25
if int(manipulate[-2:])>= 25:    
    fives = (abs(int(manipulate[-2:]))-(25*twfvs+10*tens))//5
else:
    fives = ((abs((int(manipulate[-2:]))-(10*tens)))//5)
if len(manipulate)<3:
    dollars = 0 
else:    
    dollars = manipulate[:-2]
changelist =(dollars,twfvs,tens,fives,ones)
stringchange =str(dollars)+" x $1",str(twfvs)+" x 25c",str(tens)+" x 10c",str(fives)+" x 5c",str(ones)+" x 1c"
a = 0
if change > 0:
    print("Your change is:")
while a < len(changelist):
    if changelist[a] != 0:
        print(stringchange[a])
    a += 1
    





