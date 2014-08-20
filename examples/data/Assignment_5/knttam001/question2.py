cost = eval(input("Enter the cost (in cents):\n"))
if cost>0: 
   payment = eval(input("Deposit a coin or note (in cents):\n"))
   while payment<cost:
      payment2 = eval(input("Deposit a coin or note (in cents):\n"))
      payment+=payment2
   if payment>cost:
      totchange = payment - cost
      print("Your change is:")
      num1d = totchange//100
      num25c = (totchange - (num1d*100))//25
      num10c = (totchange - (num1d*100) - (num25c*25))//10
      num5c = (totchange - (num1d*100) - (num25c*25) - (num10c*10))//5
      num1c = (totchange - (num1d*100) - (num25c*25) - (num10c*10) - (num5c*5))//1
      if num1d>0:
         print(num1d,"x","$1")
      if num25c>0:
         print(num25c,"x","25c")
      if num10c>0:
         print(num10c,"x","10c")
      if num5c>0:
         print(num5c,"x","5c")
      if num1c>0:
         print(num1c, "x","1c")      
         
   