""" program to find the change to be given by a vending machine"""
#Author: Rofhiwa Liphauphau
#Date: 16 April 2014
cost=eval(input("Enter the cost (in cents):\n")) 
def Vend():
    final=0 #assigns initial cost to variable final
    while cost>final:
        extra=eval(input("Deposit a coin or note (in cents):\n"))
        final+=extra #final is the inital deposit plus all the extra deposits
        if final>cost: #when the money enter is greater than cost the loop breaks
            break    
    change=final-cost   #calculates the change 
    e=change//100
    f=change%100
    g=f//25
    k=f%25
    l=k//10
    p=k%10
    m=p//5
    n=p%5
    o=n//1
    if change>0: #makes sure that only when there is change to be given that it gives the value of change
        print("Your change is:")
        if e !=0:#such that if there is no valu attached to the coins, it is not printed
            print(e,"x $1")
        if g !=0:
            print(g,"x 25c")
        if l !=0:
            print(l,"x 10c")
        if m !=0:
            print(m,"x 5c")
        if o !=0:
            print(o,"x 1c")

if cost>0:
    Vend()