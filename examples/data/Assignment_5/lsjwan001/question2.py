# Program to simulate a vending machine
# Wandile Lesejane
# 14 April 2014

def vending_machine():
    dcn=0
    cost=eval(input("Enter the cost (in cents):\n"))
    while  cost>dcn:
        dep=eval(input("Deposit a coin or note (in cents):\n"))
        dcn+=dep
    
    change=dcn-cost
    #calculate the change and convert to dollars and cents
    d=change//100
    c25=(change%100)//25
    c10=((change%100)%25)//10
    c5=(((change%100)%25)%10)//5
    c1=((((change%100)%25)%10)%5)//1
    #print out the change
    if d!=0 or c25!=0 or c10!=0 or c5!=0 or c1!=0:
        print("Your change is:")
    while d!=0:
        print(d,"x $1")
        break
    while c25!=0:
        print(c25,"x 25c")
        break
    while c10!=0:
        print(c10,"x 10c")
        break
    while c5 !=0:
        print(c5,"x 5c")
        break
    while c1 !=0:
        print(c1,"x 1c")
        break
vending_machine()