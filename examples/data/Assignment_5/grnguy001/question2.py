#Vending Machine Change
#Done By Guy Green

#Variables
#count variables are to count how many of each coins you would need for change
count=0
count_2=0
c=0
d=0
e=0

#Getting the cost
cost=eval(input("Enter the cost (in cents):\n"))

#If they don't give a cost print an empty string
if cost==0:
   print("")

#1st amount paid in
else:
   total_deposit=eval(input("Deposit a coin or note (in cents):\n"))
   
   
   #Getting them to pay more if they haven't paid enough
   while total_deposit<cost:
      deposit=eval(input("Deposit a coin or note (in cents):\n"))
      total_deposit+=deposit
  
   #Change
   change=total_deposit-cost
   
   #If there is change..
   if change!=0:
      print("Your change is:")
   
   #1$
   while change>=100:
      count+=1
      change-=100
   if count>0:
      print(count, "x $1")
   
   #25c
   while change>=25:
      count_2+=1
      change-=25
   if count_2>0:
      print(count_2, "x 25c")
   
   #10c
   while change>=10:
      c+=1
      change-=10
   if c>0:
      print(c, "x 10c")
   
   #5c
   while change>=5:
      d+=1
      change-=5
   if d>0:
      print(d, "x 5c")
   
   #1c
   while change>=1:
      e+=1
      change-=1
   if e>0:
      print(e, "x 1c")