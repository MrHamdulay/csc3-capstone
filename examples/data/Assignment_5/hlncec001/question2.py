#question2.py
#Cecil Hlungwana
#HLNCEC001
#16 April 2014

cost = eval(input("Enter the cost (in cents):\n")) #This is the first message if prompts. It asks for a cost.
if cost !=0: # If the cost inputted is not zero then the function should run.
    coin = eval(input("Deposit a coin or note (in cents):\n"))
    num = 0
    while coin < cost: #The 'While loop' should run when coin is less than cost.
        coins = eval(input("Deposit a coin or note (in cents):\n"))
        coin =coins + coin # It should keep on asking for coins if coin is still less than cost.
    change = coin - cost # After the loop is done running, it should calculate the change.
    len_change = len(str(change)) #This calculates the length of the change.
    if change != 0:
        if len_change >=3 :
            print("Your change is:")
            print(str(change)[:-2],"x $1")
            while len_change >= 3:
                change-=100
                len_change = len(str(change))
            while 25<= change < 100:
                change -= 25
                num+=1
            if num !=0:
                print(num,"x 25c")
            num = 0
            while 10 <= change < 25:
                change -= 10
                num+=1
            if num!=0:  
                print(num,"x 10c")
            num = 0
            while 5 <= change < 10:
                change -= 5
                num +=1
            if num!=0: 
                print(num,"x 5c")
        
        elif len_change == 2:
            print("Your change is:")
            while 25<= change < 100:
                change -= 25
                num+=1
            if num != 0:
                print(num,"x 25c")
            num = 0
            while 10 <= change < 25:
                change -= 10
                num+=1
            if num!=0:
                print(num,"x 10c")
            num = 0
            while 5 <= change < 10:
                change -= 5
                num +=1
            if num!=0:
                print(num,"x 5c")
            if 1<= change < 5: 
                print(change,'x 1c')
        
        elif len_change == 1:
            num = 0
            while 5 <= change < 10:
                change -= 5
                num +=1
            if num != 0:
                print(num,"x 5c")
            if 1 <= change < 5:
                print(change,'x 1c')