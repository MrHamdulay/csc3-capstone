#Question 3
#Tauriq Dolley
#15 April



#calculate change based on denominations

#input the cost of the item

cost = eval(input("Enter the cost (in cents):\n")) 

    
while cost != 0:   
     


#prompt user to deposit more money until amount equals/exceeds cost while making sure in correct denominations
    money = eval(input("Deposit a coin or note (in cents):\n"))
        
    total = 0
    total = total + money
    
    while cost > total:
        addition = eval(input("Deposit a coin or note (in cents):\n"))        
        total = total + addition
        
    change = total - cost
    
    dollar = 0
    twofive = 0
    ten = 0
    five = 0
    cent = 0
    
    if change != 0: 
        dollar = int((change - (change%100)) / 100)
        rem = change - (dollar * 100)
        
        twofive = int(rem // 25)
        rem = rem - (twofive*25)
        
        ten = int(rem // 10)
        rem = rem - (ten * 10)
        
        five = int(rem // 5)
        rem = rem - (five * 5)
        
        cent = int(rem)
        rem = rem - cent
    if change != 0:    
        print("Your change is:")    
        
        if dollar != 0:
            print(dollar," x $1",sep='')
        if twofive != 0:
            print(twofive," x 25c",sep='')
        if ten != 0:
            print(ten," x 10c",sep='')
        if five != 0:
            print(five," x 5c",sep='')
        if cent != 0:
            print(cent," x 1c",sep='')
    
    cost = 0
