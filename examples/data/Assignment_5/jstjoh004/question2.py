# a program to simulate a vending machine 
# and calculate change based on the amount paid
# hendrik Joosten
# 17 april 2014

# getting the cost from the user and evaluating it
user_cost = eval(input("Enter the cost (in cents):\n"))

# initializing the variable sum wich represents 
# the amount of money the user inserted
sum  = 0 

# ask the user for more money until the cost is met
while sum < user_cost:
      user_money = eval(input("Deposit a coin or note (in cents):\n"))
      sum = sum + user_money

# determining the total change that the user will recieve
user_change = sum - user_cost

# if the user has change this if will be called and the change 
# will be worked out otherwise nothing will happen
if user_change != 0:
      print("Your change is:")
      
      # the amount of dollars in the users change
      dollars = user_change//100 
      user_change = user_change - (dollars*100)
      
      # the amount of twenty five cent coins in the users change
      twentyfives = user_change//25
      user_change = user_change - (twentyfives*25)
      
      # the amount of ten cent coins in the users change
      tens = user_change//10
      user_change = user_change - (tens*10)
      
      # the amount of five cent coins in the users change
      fives = user_change//5
      user_change = user_change -(fives*5)
      
      # the amount of one cent coins in the users change
      ones = user_change//1
      user_change = user_change - (ones*1)
      
      # list containing the amount of various notes and coins  
      # the user must recieve (these are all variables)
      list = [dollars,twentyfives,tens,fives,ones]
      # a list representing the coins and note names the the user will recieve
      list_of_signs = ["$1","25c","10c","5c","1c"]

      # a for lop to go through above metioned lists
      for i in range(len(list)):
            if list[i] > 0:
                  print(list[i],"x",list_of_signs[i])

