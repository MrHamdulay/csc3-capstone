cost=eval(input("Enter the cost (in cents):\n"))
deposit=0

while(deposit<cost):
    deposit+=eval(input("Deposit a coin or note (in cents):\n"))
change=deposit-cost

#Count the number of each coin required
if(change>0):
    print("Your change is:")
if(change>=100):
    num_100=change//100
    print(num_100,"x $1")
change=change%100

if(change>=25):
    num_25=change//25
    print(num_25,"x 25c")
change=change%25

if(change>=10):
    num_10=change//10
    print(num_10,"x 10c")
change=change%10

if(change>=5):
    num_5=change//5
    print(num_5,"x 5c")
change=change%5

if(change>=1):
    num_1=change//1
    print(num_1,"x 1c")
