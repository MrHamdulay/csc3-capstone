# Question 2 Vending machine
# Jaren Hendricks
# 16 April 2014


# Gets the input from the user
cost = eval (input("Enter the cost (in cents):\n"))

# Declaring variables and assigning the variables to zero
a = 0
b = 0
c = 0
d = 0
e = 0
count = 0
change = 0

# Loop to calculate the change
while count < cost:
         deposit = eval (input("Deposit a coin or note (in cents):\n"))
         count = count + deposit 
         change = count - cost
         if (change - 100 > 0):
                  a = change//100
                  change = change%100
         if (change - 25 >= 0):
                  b = change//25
                  change = change%25
         if (change - 10 >= 0):
                  c = change//10
                  change = change%10
         if (change - 5 >= 0):
                  d = change//5
                  change = change%5
         if (change - 1 >= 0):
                  e = change//1
                  change = change%1
              

# output statments -> Checks whether each variable is greater than 0 and counts the number of coins. 
if (count-cost) > 0:
         print("Your change is:")
if a > 0:
         print(a, "x", "$1", sep = " ") 
if b > 0:
         print(b, "x", "25c", sep = " ")         
if c > 0: 
         print(c, "x", "10c", sep = " ")
if d > 0:
         print(d, "x", "5c", sep = " ")
if e > 0:
         print(e, "x", "1c", sep = " ")


        
                 
