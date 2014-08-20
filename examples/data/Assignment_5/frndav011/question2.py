"""David Fransch
Assignment 5- Q2
14-04-2014"""

#Input
cost = eval(input("Enter the cost (in cents):\n"))

   #cost = eval(input("Enter the cost (in cents):\n"))
total = 0
#Keeps asking for deposit until toatl is matched or exceeded
if cost != 0:
   while cost>total:
      pay = eval(input("Deposit a coin or note (in cents):\n"))
      total = total +pay
   #Calculates change   
   change = total - cost   
   num1=0
   num2=0
   num3=0
   num4=0
   num5=0
   #Sorts what change should be given
   if change>=100:
       while change>=100:
           change-=100
           num1+=1
       
       
   if change>=25:
       while change>=25:
           change-=25
           num2+=1
       
      
   if change>=10 :
       while change>=10:
           change-=10
           num3+=1
       
       
   if change>=5 :
       while change>=5:
           change-=5
           num4+=1
       
       
   if change>=1 :
       while change>=1:
           change-=1
           num5+=1
       
       
   #Returns/prints change and attaches relative string
   if total != cost:
      print("Your change is:")
      if num1>0:
         print(num1,"x $1")
      if num2>0:
         print(num2,"x 25c")
      if num3>0:
         print(num3,"x 10c")
      if num4>0:
         print(num4,"x 5c")
      if num5>0:
         print(num5,"x 1c")
