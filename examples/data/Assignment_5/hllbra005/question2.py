#Assignment 5: Question 2, Vending machine simulation
#Brandon Hall (HLLBRA005)
#17/04/2014

def Main(): #This function will call on everything else

    amount = 0
    
    print("Enter the cost (in cents):")
    cost = eval(input())
    
    while(amount < cost): #While the amount entered is smaller then the initial cost given, the program will continue to ask the user to enter in more monney
        
        print("Deposit a coin or note (in cents):")
        amount = amount + eval(input())
    
    calc(cost,amount) #Parses variables to cost function and runs it
    
def calc(cost,amount):
    
    change = amount - cost 

    if(change != 0):
        print("Your change is:")
    
    while(change != 0):
        
                        
        if(change >= 100):    
            
            one = change // 100
            change = change - (100 * one)
            print(str(int(one)) + " x $1")
            
        elif((change < 100) and (change >= 25)):
        
            twentyfive = change // 25
            change = change - (25 * twentyfive)
            print(str(int(twentyfive)) + " x 25c")
            
                   
        elif((change < 25) and (change >= 10)):   
           
            ten = change // 10
            change = change - (10 * ten)
            print(str(int(ten)) + " x 10c")
            
        elif((change < 10) and (change >= 5)):    
            
            five = change // 5
            change = change - (5 * five)   
            print(str(int(five)) + " x 5c")
   
        elif((change < 5)and (change >=1)):
            
            change = 0
        
        elif(change < 1):
        
            uno = change // 1
            change = change - (1 * uno)
            print(str(int(uno)) + " x 1c")        
Main()    