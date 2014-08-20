"""this program calculates the change based on the amount paid for a specific item in a vending machine
quincy cele 
14 april 2914"""

cost=eval(input("Enter the cost (in cents):\n"))
if cost==0:
   print("",end="")
else:
   money_entered= eval(input("Deposit a coin or note (in cents):\n"))

   accumulative_money=money_entered
   
   while accumulative_money<cost:
      add_money=eval(input("Deposit a coin or note (in cents):\n"))
      accumulative_money+= add_money
      
         
   if accumulative_money>cost:
      change=accumulative_money-cost
      if change>=0:
         print("Your change is:")
       
         dollar=change//100    
         if dollar>0:
            print(dollar,"x $1")
         difference=change-(dollar*100)
         
         quarter=difference//25        
         if quarter>0:
            print(quarter,"x 25c")
         difference1=difference-(quarter*25)
         
         dime=difference1//10        
         if dime>0:
            print(dime,"x 10c")
         difference2=difference1-(dime*10)
         
         nickel=difference2//5        
         if nickel>0:
            print(nickel,"x 5c")
           
         penny=difference2-(nickel*5)
         if penny>0:
            print(penny,"x 1c")
           
           
      else:
         print("")

    
    
        
    
    

    
        