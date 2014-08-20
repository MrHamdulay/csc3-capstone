cost = eval(input("Enter the cost (in cents):\n"))
pay = 0
if cost!=0:
    
    pay = eval(input("Deposit a coin or note (in cents):\n"))
diff = cost -pay

paid = 0

change = [0]*5
values = ["1c", "5c", "10c", "25c", "$1"]
cnt = 4

while diff>0 and cost!=0:
    
    pay = eval(input("Deposit a coin or note (in cents):\n"))
    diff -=pay

pdiff = abs(diff)


while paid == 0 and (pdiff)!=0 and cost!=0:
    
    if (pdiff) - 100 >0:
        pdiff -=100
        change[4]+=1
       
    elif(pdiff)-100==0:
        change[4]+=1
        paid = 1
    elif (pdiff) - 25 >0:
        pdiff -=25
        change[3]+=1
    elif(pdiff)-25==0:
        change[3]+=1
        paid = 1
    elif (pdiff) - 10 >0:
        pdiff -=10
        change[2]+=1
    elif(pdiff)-10==0:
        change[2]+=1
        paid = 1
    elif (pdiff) - 5 >0:
        pdiff -=5
        change[2]+=1
    elif(pdiff)-5==0:
        change[2]+=1
        paid = 1
    elif (pdiff) - 25 >0:
        pdiff -=25
        change[1]+=1
    elif(pdiff)-1==0:
        change[1]+=1
        paid = 1
    
    
    
    
if(pdiff!=0):
    
    print("Your change is:")
    for i in range(4,-1,-1):
        if change[i]!=0:
            print(change[i], "x" , values[i])
        
     
     
