cost=eval(input("Enter the cost (in cents):\n"))    #ask user for cost
money=0                   

while(money<cost):      #continue asking for money until cost is = or greater than cost
    money+=eval(input("Deposit a coin or note (in cents):\n"))   #ask user for deposit
change=money-cost                 #calculate change

#Count the number of each different coin required
if(change>0):
    print("Your change is:")
if(change>=100):
    num_100=change//100
    print(num_100,"x $1")
change=change%100
if change>=25:
    twenty_five=change//25
    print(twenty_five,"x 25c")
change=change%25
if change>=10:
    ten_cent=change//10
    print(ten_cent,"x 10c")
change=change%10
if change>=5:
    five_cent=change//5
    print(five_cent,"x 5c")
change=change%5
if change>=1:
    one=change//1
    print(one,"x 1c")
