cost = eval(input("Enter the cost (in cents):\n"))

value = 0
while (value<cost):
    value = value + eval(input("Deposit a coin or note (in cents):\n"))

change = value-cost
if (value != cost and cost!= 0):
    print("Your change is:")

while(change!=0):
    if (change//100 != 0):
        num = change//100
        change = change%100
        print(num, "x $1")
    elif(change//25 !=0):
        num = change//25
        change = change%25
        print(num, "x 25c")
    elif(change//10 !=0):
        num = change//10
        change = change%10 
        print(num, "x 10c")
    elif(change//5 !=0):
        num = change//5
        change = change%5
        print(num, "x 5c")
    else:
        print(change, "x 1c")
        change = 0
    
