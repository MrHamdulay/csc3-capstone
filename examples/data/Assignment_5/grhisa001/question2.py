""" Bella gorham
vending machine change program
question2
14/04/2014"""

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    if cost != 0:
        
        deposit= eval(input("Deposit a coin or note (in cents):\n"))
        while deposit < cost:
            deposit2= eval(input("Deposit a coin or note (in cents):\n"))
            deposit+=deposit2
        

        rawchange= deposit-cost
        onecoins= 0
        quatercoins= 0
        tenscoins = 0
        fivecoins = 0
        centcoins = 0
        onecoins = rawchange//100
    
        quatercoins = rawchange % 100 // 25
        tencoins = rawchange % 100 % 25 // 10
        fivecoins = rawchange % 100 % 25 % 10 // 5
        centcoins = rawchange % 100 % 25% 10 % 5
    
    
        if deposit - cost != 0:
            print("Your change is:")
        if onecoins >= 1:
            print(onecoins,"x $1")
        if quatercoins >= 1:
            print(quatercoins,"x 25c")
        if tencoins >= 1:
            print(tencoins,"x 10c")
        if fivecoins >= 1:
            print(fivecoins,"x 5c")
            
        if centcoins >= 1:
            print(centcoins,"x 1c")
    
    
    
main()
    