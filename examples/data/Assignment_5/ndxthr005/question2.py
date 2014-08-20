"""question2: program, vending machine 
thrianka naidoo
ndxthr005"""

cost = eval(input("Enter the cost (in cents):\n"))          #Input from the user
dep = 0
x = True
while x:
        if cost == 0:
                break
        else:
                dep = eval(input("Deposit a coin or note (in cents):\n")) 
                x = False

while dep<cost:                                             #Reloop until the deposit for the cost is met  
        x = eval(input("Deposit a coin or note (in cents):\n"))
        dep = dep + x
    
change = dep - cost                                         #Change is given in coins only ... 1c,5c,10c,25c,$1 --- 100c makes $1
if change>0:
        print("Your change is:")
    
dollars = change//100                                       #$1 -- use integer division, it rounds downwards
if dollars>=1:
        print(dollars,"x $1")   

change = (change-(dollars*100))                             #change in cents after dollars are removed

if change>=25:                                              #25c
        cents_25 = (change//25)
        print(cents_25,"x 25c")
        change = change - (cents_25*25)
                
if change>=10:                                              #10c
        cents_10 = change//10                          
        if cents_10>0:
                print(cents_10,"x 10c")
                change = change - (cents_10*10)
    
if change>=5:
        cents_5 = change//5                                 #5c
        if cents_5>0:
                print(cents_5,"x 5c")
                change = change - (cents_5*5)

if change>=1 and change<5:                                  #1c
        print(change,"x 1c")
        change = change - (change*1)

#print(dep)
#print(cost)
#print(change)