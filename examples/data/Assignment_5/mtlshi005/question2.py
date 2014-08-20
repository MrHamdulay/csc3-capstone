#change output in different amounts
#Shivaan Motilal
#13/04/14




cost=eval(input("Enter the cost (in cents):\n"))

y=0

while y<cost:
   
      deposit=eval(input("Deposit a coin or note (in cents):\n"))
      y+=deposit
      
change=abs(y-cost)
if change>0:
      print("Your change is:")



oned=change//100
if (change>=100):
      print(oned,"x","$1")
      change=change%100


if (change>=25):
      twentyfive=change//25
      print(twentyfive,"x","25c")
      change=change%25 

if (change>=10):
      ten=change//10
      print(ten,"x","10c")
      change=change%10

if (change>=5):
      five=change//5
      print(five,"x","5c")
      change=change%5

if change>=1:
      one=change//1
      print(one,"x","1c")






       
