count=[0,0,0,0,0,0,0]
list=[500,200,100,50,20,10,5]
#GVNMER006
#2014-04-16
def vending():
    i=0
    cost=input("Enter the cost (in cents):\n")
    cost=eval(cost)
    deposit=0
    while deposit<cost:
        amount=eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=amount
    change=deposit-cost
    
    while(change!=0):
        while((change>=int(list[i]))):
            change=change-int(list[i])
            count[i]=str(int(count[i])+1)
        i+=1
def display():
    change=False
    for i in range(7):
        if(int(count[i])>0):
            change=True
    if(change):
        print("Your change is:")
        for i in range(7):
            if(int(count[i])>0 and i==0):
                print(count[i],"x","R5")
            elif(int(count[i])>0 and i==1):
                print(count[i],"x","R2")
            elif(int(count[i])>0 and i==2):
                print(count[i],"x","R1")
            elif(int(count[i])>0 and i==3):
                print(count[i],"x","50c")
            elif(int(count[i])>0 and i==4):
                print(count[i],"x","20c") 
            elif(int(count[i])>0 and i==5):
                print(count[i],"x","10c")   
            elif(int(count[i])>0 and i==6):
                print(count[i],"x","5c")            
vending()        
display()
        
        
        
        
    
    