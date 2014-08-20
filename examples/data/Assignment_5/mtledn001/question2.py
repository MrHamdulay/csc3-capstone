#Vending machine
cost = eval(input('Enter the cost (in cents):\n'))
if cost!=0:
   coin =  eval(input('Deposit a coin or note (in cents):\n'))
   while coin<cost:
      coin +=  eval(input('Deposit a coin or note (in cents):\n'))

   change = coin-cost
   if change!=0:
       print('Your change is:')
       if change>=100:
           print(change//100,'x $1')
           change = change-((change//100)*100)
           
       if change>=25:
           print(change//25,'x 25c')
           change = change-((change//25)*25)  
           #print(change)
       if change>=10:
           print(change//10,'x 10c')
           change = change-((change//10)*10)
       if change>=5:
           print(change//5,'x 5c')
           change = change-((change//5)*5)
       if change>=1:
           print(change//1,'x 1c')
           #change = change-((change//1)*1)
        
        



































