"""calculating the physical change of a transaction
danica van der zandt
14 april 2014"""

deposited=0

#enter the cost
cost=eval(input("Enter the cost (in cents):\n"))

#get deposits until deposited equals or exceeds cost
while deposited < cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    deposited+=deposit
    if deposit ==0:
        break
    else:
        continue
    



#calculating the physical change            

if cost == 0:
    print()
    
else:
    rem=deposited-cost
    if rem==0:
        print()
    else:
        print("Your change is:")
   
        
        #if there is change to be given   
        if rem >= 100:
            d=rem//100
            d=str(d)
            print(d+" x $1")
            rem=rem-(int(d)*100)
            
        if  25 <= rem < 100:
            t=rem//25
            t=str(t)
            print(t+" x 25c")
            rem=rem-(int(t)*25)
            
        if 10 <= rem < 25:
            tens=rem//10
            tens=str(tens)
            print(tens+" x 10c")
            rem=rem-(int(tens)*10)
            
        if 5 <= rem < 10:
            fives=rem//5
            fives=str(fives)
            print(fives+" x 5c")
            rem=rem-(int(fives)*5)
            
        else:
            if rem==0:
                pass
            else:
                print(str(rem)+" x 1c")
                
                

            