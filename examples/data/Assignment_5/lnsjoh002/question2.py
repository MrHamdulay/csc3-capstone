cost = eval(input("Enter the cost (in cents):\n"))

tot = 0

while tot < cost :
    insert = eval(input("Deposit a coin or note (in cents):\n"))
    tot += insert
    
    
#Now calculate change needed 
change = tot - cost
if change!=0:
    print("Your change is:")


Num_of_1dollar = change//100
if Num_of_1dollar !=0:
    print(Num_of_1dollar,"x $1")
change = change - (Num_of_1dollar * 100)

Num_of_25c = change//25
if Num_of_25c != 0:
    print(Num_of_25c, "x 25c")
change = change - (Num_of_25c *25)

Num_of_10c = change//10
if Num_of_10c != 0:
    print(Num_of_10c, "x 10c")
change = change - (Num_of_10c * 10)

Num_of_5c = change//5
if Num_of_5c != 0:
    print(Num_of_5c, "x 5c")
change = change - (Num_of_5c * 5)

Num_of_1c = change//1
if Num_of_1c != 0:
    print(Num_of_1c, "x 1c")
    


    

