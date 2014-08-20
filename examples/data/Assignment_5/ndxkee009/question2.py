#Keegan Naidoo
#NDXKEE009
#16 April 2014

cost=eval(input("Enter the cost (in cents):\n"))     #Input cost

original_cost=cost

stop=True               #Boolean variable to enter and exit loop

while(stop==True):      #Loop until stop is False
    
    if cost==0:         # Exception handling if cost is 0 stop program
        stop=False    
        break
        
    depo=eval(input("Deposit a coin or note (in cents):\n"))   #Input deposit
    cost+=-depo                                                #Changing cost to subtract deposit from it each time
    
    if (cost<=0):                                              #If there is a cost continue
        
        change=cost*-1                #Calculate change
        change_dollar=change//100     #Calculate change in dollars
        
        if change==0:                 #If there is no change stop the program
            stop==True
        
        if change != 0:               #If there is change continue
            print("Your change is:")
        
        if (change_dollar>=1):        #If there is change in dollars continue
            print(change_dollar,"x $1")   
        
        change+=-(change_dollar*100)
        
        if (change>=25):              #If there is change in 25c increments continue                              
            c25 = (change//25)
            print(c25,"x 25c")
            change +=- (c25*25) 
        
        if(change>=10):               #If there is change in 10c increments continue
            c10 = (change//10)
            print(c10,"x 10c")
            change += - (c10*10)       
        
        if (change>=5):              #If there is change in 5c increments continue
            c5 = change//5                                     
            if c5>0:
                print(c5,"x 5c")
                change += - (cents_5*5)
        
        if change>=1 and change<5:   #If there is change in 1c increments continue                               
            print(change,"x 1c")
            change +=- (change*1)
        
                                       
        #dollar=str(change)
        #print(t)
        
        #dollar_str=dollar[0:dollar.find('.')]
        #print(t1)
        
        #dollar_int=int(dollar_str)
        #print("Your change is:\n")
        #print("$",change,sep='')
        
        stop=False         #Stop program
