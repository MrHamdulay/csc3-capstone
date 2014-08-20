#NGMTAS001
#Question2
#Assignment5

cost = eval(input("Enter the cost (in cents):\n"))
deposit = 0
while deposit<cost:
    paid = eval(input("Deposit a coin or note (in cents):\n"))
    deposit = deposit+paid
change = deposit -cost
original = change
ch1,ch2,ch3,ch4,ch5,ch6 = 0,0,0,0,0,0
count =0

if change>=100:
    ch1 = change//100
    change = change -(ch1*100) 
    if (change>=25):
        ch2 = change//25
        change = change -(ch2*25)
        if (change>=10):
            ch3 = change//10
            change = change -(ch3*10) 
            if (change>=5):
                ch4 = change//5 
                change = change -(ch4*5)  
                if (change>=2):
                    ch5 = change//2 
                    change = change -(ch5*2)  
                    if (change>=1):
                        ch6 = change//1 
                        change = change -(ch6*1)                          
                 
elif (change >=25):
    ch2 = change//25
    change = change -(ch2*25)
    if (change>=10):
        ch3 = change//10
        change = change -(ch3*10) 
        if (change>=5):
            ch4 = change//5 
            change = change -(ch4*5)  
            if (change>=2):
                ch5 = change//2 
                change = change -(ch5*2)  
                if (change>=1):
                    ch6 = change//1 
                    change = change -(ch6*1)      

elif (change>=10):
    ch3 = change//10
    change = change -(ch3*10) 
    if (change>=5):
        ch4 = change//5 
        change = change -(ch4*5)  
        if (change>=2):
            ch5 = change//2 
            change = change -(ch5*2)  
            if (change>=1):
                ch6 = change//1 
                change = change -(ch6*1)      

elif (change>=5):
    ch4 = change//5 
    change = change -(ch4*5)  
    if (change>=2):
        ch5 = change//2 
        change = change -(ch5*2)  
        if (change>=1):
            ch6 = change//1 
            change = change -(ch6*1) 
            
elif (change>=2):
    ch5 = change//2 
    change = change -(ch5*2)  
    if (change>=1):
        ch6 = change//1 
        change = change -(ch6*1) 

elif (change>=1):
    ch6 = change//1 
    change = change -(ch6*1) 
 
 
tmp = str(ch1)+","+str(ch2)+","+str(ch3)+","+str(ch4)+","+str(ch5)+","+str(ch6)
part =tmp.split(",")

if cost !=0 and original !=0:
    print("Your change is:")

count = 0
for x in part:
    if (x != "0" and count == 0):
        print (x, "x $1")
    if (x != "0" and count == 1):
        print (x, "x 25c")        
    if (x != "0" and count == 2):
        print (x, "x 10c")
    if (x != "0" and count == 3):
        print (x, "x 5c")      
    if (x != "0" and count == 4):
        print (x, "x 2c")
    if (x != "0" and count == 5):
        print (x, "x 1c")           
    count = count+1
  
    
    

      
      
      
      