#Code to calculate change
#Saul Bloch
#14 April 2014

#asks for cost
cost = eval(input("Enter the cost (in cents):\n"))
if cost > 0:
    #asks for first note/coin spent
    total = eval(input("Deposit a coin or note (in cents):\n"))
    
    oneDollar = 0
    twentyFive = 0
    ten = 0
    five = 0
    one = 0
    
    while cost>total: #asks for all note/coin spent til spent enough
        temp = eval(input("Deposit a coin or note (in cents):\n"))
        total += temp
    
    difference = total-cost
    difference2 = total-cost
    
    #The whiles work out how many of each note/coin needs to be included to work out change 
    while ((difference/100)>=1):
        oneDollar +=1
        difference -= 100
    
    while ((difference/25)>=1):
        twentyFive +=1
        difference -= 25
    
    while ((difference/10)>=1):
        ten +=1
        difference -= 10
    
    while ((difference/5)>=1):
        five +=1
        difference -= 5
    
    while ((difference/1)>=1):
        one +=1
        difference -= 1
        
    if difference2 > 0: #if there is change, print out all the change
        print("Your change is:")
        if (oneDollar > 0):
            print(str(oneDollar)+" x $1")
        if (twentyFive > 0):
            print(str(twentyFive)+" x 25c")
        if (ten > 0):
            print(str(ten)+" x 10c")
        if (five > 0):
            print(str(five)+" x 5c")
        if (one > 0):
            print(str(one)+" x 1c")