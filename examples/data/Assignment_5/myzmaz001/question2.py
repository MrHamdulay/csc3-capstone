"""
Mazwi Myeza    Assignment5
15 March 2014
Question 2 """

#ask for cost

cost = int(input("Enter the cost (in cents):\n"))
paid = 0
#getting the required amount of money from user
while paid < cost:
    deposit = int(input("Deposit a coin or note (in cents):\n"))
    paid += deposit
# getting change    
change = paid - cost
i = change//100
j = (change%100)//25
k = ((change%100)%25)//10
l = (((change%100)%25)%10)//5
u = ((((change%100)%25)%10)%5)//1

#printing change
if change != 0:
    print("Your change is:")
    if i != 0:
        print(i,"x $1")
    if j !=0:
        print(j,"x 25c")
    if k != 0:
        print(k,"x 10c")
    if l != 0:
        print(l,"x 5c")
    if u != 0:
        print(u,"x 1c")