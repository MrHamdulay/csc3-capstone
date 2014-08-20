""" Vending machine program, to give change 
Richard Marais
14/04/14"""

def vendingmachine():    
        
        cost = eval(input('Enter the cost (in cents):\n'))        #input cost of product       
        if cost >0:
                d = eval(input('Deposit a coin or note (in cents):\n'))    #input the value of the payment
                j=0
                while d < cost:                      #to prompt to pay more if value is too low
                        d += eval(input('Deposit a coin or note (in cents):\n'))
                        
                j = d-cost                             #to give change, work out the difference
                if j > 0:                            #use remainder and a run of 'if' statements to calculate the change
                   print("Your change is:") 
                   f = 0
                   if j/100 >= 1:                       
                        print(int(j/100),'x $1')
                        j = j%100
                   if j/25 >= 1:
                        print(int(j/25),'x 25c')
                        j = j%25
                   if j/10 >= 1:
                        print(int(j/10),'x 10c')
                        j= j%10
                   if j/5 >= 1:
                        print(int(j/5),'x 5c')
                        j = j%5
                   if j/1 >= 1:
                        print(j,'x 1c')
                                               
                
            
vendingmachine()
