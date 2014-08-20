#Dhriven Hamlall

money=[100,25,10,5,1] #1c, 5c, 10c, 25c, $1
position=[0,0,0,0,0]


#------------------------------------------------------------------------------------------------------------------
def Work_out_change():
    i=0
    cost=eval(input("Enter the cost (in cents):\n"))
    deposit=0
    while deposit<cost:
        amount=eval(input("Deposit a coin or note (in cents):\n"))
        deposit=deposit+amount
    change=deposit-cost
#------------------------------------------------------------------------------------------------------------------
    
    while(change!=0):
        while((change>=int(money[i]))): #money[0]=100
            change=change-int(money[i])
            position[i]=str(int(position[i])+1)
        i=i+1
        
#------------------------------------------------------------------------------------------------------------------------        
def display():
    change=False
    for i in range(5):
        if(int(position[i])>0):
            change=True
            
    if(change):
        print("Your change is:")
        for i in range(5):
            
            if(int(position[i])>0 and i==0):
                print(position[i],"x","$1")
             
            elif(int(position[i])>0 and i==1):
                print(position[i],"x","25c") 
                
            elif(int(position[i])>0 and i==2):
                print(position[i],"x","10c")   
                
            elif(int(position[i])>0 and i==3):
                print(position[i],"x","5c")  
                
            elif(int(position[i])>0 and i==4):
                print(position[i],"x","1c") 
                
#-------------------------------------------------------------------------------------------------------------------------------                
Work_out_change()        
display()