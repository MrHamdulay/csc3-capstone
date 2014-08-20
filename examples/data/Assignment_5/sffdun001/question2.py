# Question 2- Assignment 5
# Duncan Saffy
# 14/04/2014
cost= eval(input("Enter the cost (in cents):\n"))
sumdep=0
while sumdep < cost: 
    dep= eval(input("Deposit a coin or note (in cents):\n"))
    sumdep= sumdep+dep
diff= sumdep-cost
if diff==0:
    print("")
elif diff!=0:
    print("Your change is:")
    if diff>=100:
        print(diff//100,"x $1")
    diff= diff%100
    if diff>= 25:
        print(diff//25,"x 25c")
    diff=diff%25
    if diff>=10:
        print(diff//10,"x 10c")
    diff= diff%10
    if diff>=5:
        print("1 x 5c")
    diff= diff%5
    if diff>=1:
        print(diff,"x 1c")
        