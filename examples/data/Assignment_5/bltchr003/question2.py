"""Assignment 5
Vending machine
Chris Bolton
"""

#Enter cost of an item
cost = eval( input ( "Enter the cost (in cents):\n" ))

if cost <=0:
       print("")
        
else:
       deposit= eval (input ( "Deposit a coin or note (in cents):\n" ) )

       i = cost-deposit
       while i>0:
              extra= eval (input ( "Deposit a coin or note (in cents):\n" ) )
              deposit = deposit + extra
              if deposit >= cost:
                     break
       change = deposit-cost
      #Calculates the change
       dollar = change//100
       quarter = ( change%100 ) // 25
       dimes = ( ( change % 100 ) % 25) // 10
       nickels = ( ( (change % 100 ) % 25) %10 ) //5
       pennies = ( ( ( (change % 100) % 25) % 10) % 5)  

      #Outputs the change:
       if change == 0:
              print("")
       else:
              print( "Your change is:" )
              if dollar > 0:
                     print( dollar, "x $1" )
              if quarter > 0:
                     print( quarter, "x 25c" )
              if dimes > 0:
                     print( dimes, "x 10c" )
              if nickels > 0:
                     print( nickels, "x 5c" )
              if pennies > 0:
                     print( pennies, "x 1c")
