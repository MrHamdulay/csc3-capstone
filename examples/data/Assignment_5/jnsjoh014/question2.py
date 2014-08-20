def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    paid = 0
    while paid<cost:
        val = eval(input("Deposit a coin or note (in cents):\n"))
        paid+=val
    if paid>cost:
        change = paid-cost
        print("Your change is:")
        
        amDol = 0
        amTwF = 0
        amTen = 0
        amFiv = 0
        amOne = 0        
        
        if change>=100:
            amDol = change//100
            print(amDol,"x $1")
            change = change-amDol*100
        if change>=25:
            amTwF = change//25
            print(amTwF,"x 25c")
            change = change-amTwF*25
        if change>=10:
            amTwF = change//10
            print(amTwF,"x 10c")
            change = change-amTwF*10          
        if change>=5:
            amFiv = change//5
            print(amFiv,"x 5c")
            change = change-amFiv*5  
        if change>=1:
            amOne = change
            print(amOne,"x 1c")
                                
           
     
if __name__=="__main__":
    main()