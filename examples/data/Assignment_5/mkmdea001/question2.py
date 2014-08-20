#prog for vending machine 
#ass5q2
# function for calculating change from a vending machine 
def vendmach():
   #get cost from user 
   cost = eval(input('Enter the cost (in cents):\n'))
   #if cost is more than 0 then execute the prograam
   if cost>0:
      #get deposit
      dep = eval(input('Deposit a coin or note (in cents):\n'))
      #calculate the change
      change = dep - cost
      a=change//100
      
      y=('Your change is:')
         
      #if cost is less than deposit execute the following         
      if cost < dep:
         print(y)
         change
         #if change is divisible by 100 then print the answer multiplied by $1
         if a:
            print(change//100, 'x $1')
         #find the remaining change which is equal to the remainder of the change divided by 100   
         h = change%100
         #if change is divisible by 25 then print the answer multiplied by 25c
         if h//25:
            print(h//25, 'x 25c')
         #find the remaining change which is equal to the remainder of the change divided by 25    
         x = h%25
         #if change is divisible by 10 then print the answer multiplied by 10c
         if x//10:
            print(x//10, 'x 10c')
         #find the remaining change which is equal to the remainder of the change divided by 10   
         t = x%10 
         #if change is divisible by 5 then print the answer multiplied by 5c
         if t//5:
            print(t//5, 'x 5c')
         #find the remaining change which is equal to the remainder of the change divided by 5   
         f = t%5
         #if change is divisible by 1 then print the answer multiplied by 1c
         if f//1:
            print(f//1, 'x 1c')
      #if cost is more than deposit then ask the user for more deposit and and perform a similar calculation for change as before   
      if cost>dep:
         dep1=dep
         #as long as cost is more than deposit keep asking user for more deposit 
         while cost>dep1:
               
            dep2 = eval(input('Deposit a coin or note (in cents):\n'))
            dep1+=dep2
         if dep1!=cost:
            if cost < dep1:
               change1=dep1-cost
               print(y)
        
               if change1//100:
                  print(change1//100, 'x $1')
               h = change1%100
               if h//25:
                  print(h//25, 'x 25c')
               x = h%25
               if x//10:
                  print(x//10, 'x 10c')
               t = x%10   
               if t//5:
                  print(t//5, 'x 5c')
               f = t%5
               if f//1:
                  print(f//1, 'x 1c')         
         
         
         
         
     
         

      
vendmach()
