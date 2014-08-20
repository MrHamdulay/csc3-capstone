#GPXSHI001
#17th April
#Q2

cost = eval(input("Enter the cost (in cents):\n"))

paid = 0


while paid < cost:
   y = eval(input("Deposit a coin or note (in cents):\n"))
   paid += y
change = paid - cost

if change != 0:
   print("Your change is:")



countdollar = 0
while change >= 100:
   change -= 100
   countdollar += 1 

count2quarter = 0
while change >= 25:
   change -= 25
   count2quarter +=  1
   
   
count2ten = 0
while change >= 10:
   change -= 10
   count2ten +=  1
   
   
count2five = 0
while change >= 5:
   change -= 5
   count2five += 1
    
   
count2one = 0
while change >= 1:
   change -= 1
   count2one += 1
   
   
if countdollar > 0  or  (count2quarter > 0) or (count2ten > 0) or (count2five > 0) or (count2one > 0):
   if countdollar > 0:
      print(countdollar, "x $1")
   if count2quarter > 0:
      print(count2quarter, "x 25c")
   if count2ten > 0:
      print(count2ten, "x 10c")
   if count2five > 0:
      print(count2five, "x 5c")
   if count2one > 0:
      print(count2one, "x 1c")


