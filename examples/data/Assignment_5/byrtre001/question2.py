""" Calculate change after depositing cash for an item
Trevor Byaruhanga
18 April 2014"""

# input question prompting the user to enter an amount
cost=eval(input('Enter the cost (in cents):''\n'))
total=0
# if the total change is the less than the cost, then prompt the user for more change.
while total<cost:
   change=eval(input('Deposit a coin or note (in cents):''\n')) 
#add the current total amount to the change   
   total=total+change
#if the total is more but not equal to the cost then display the change.
if total!=cost:
   print('Your change is:')
new_change=total-cost
dollar=new_change//100
cents25=((new_change%100)//25)
cents10=(((new_change%100)%25)//10)
cents5=((((new_change%100)%25)%10)//5)
cents1=((((new_change%100)%25)%10)%5)
# prints the change in dollars and cents if the condition is met
if dollar>0:
   print(dollar,'x','$1')
if cents25>0:
   print(cents25,'x','25c')
  
if cents10>0:
   print(cents10,'x','10c')
if cents5>0:
   print(cents5,'x','5c')
if cents1>0:
   print(cents1,'x','1c')   
