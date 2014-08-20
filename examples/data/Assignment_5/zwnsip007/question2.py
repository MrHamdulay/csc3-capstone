'''programme to get the change
Siphesihle Zwane
15-04-14'''

#input the price of item 
price= eval(input("Enter the cost (in cents):"'\n'))
hey=0
while hey < price:
#input the value of each coin deposit   
    insert=eval(input("Deposit a coin or note (in cents):"'\n'))
    hey+=insert
#calculations for different not values
change=hey-price
dollar=change//100
quarter=(change%100)//25
tencents=((change%100)%25)//10
cents=(((change%100)%25)%10)
#for all amounts greater  or equal to 100
if change==0:
    print("")
if change>=100:
    print("Your change is:")
    print(dollar,"x $1")
    if quarter>0:
        print(quarter, "x 25c")
    if tencents>0:
        print (tencents, "x 10c")
    if cents !=0:
        print(cents, "x 1c")
#for all amounts between 100 and including 25 
if change<100 and change>=25 :
    print("Your change is:")
    print(quarter, "x 25c")
    if tencents>0:
        print (tencents, "x 10c")
    if cents!=0:
        print(cents, "x 1c")
  
#for all amounts less than 25 including 10        
if change<25 and change>=10:
    print("Your change is:")
    print (tencents, "x 10c")
    if cents!=0:
        print(cents, "x 1c")
#for all amounts smaller than 10        
if change<10 and change!=0:
    print("Your change is:")
    print(cents, "x 1c")
  
    
    
        
    

    

    

            
            
            
            
   