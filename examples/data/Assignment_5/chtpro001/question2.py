# Gadziraiushe Bangure: BNGGAD001
# Assignment 5: Program to simulate a vending machine
# Written by ~Shay~
# Date: 18/04/2014



C=eval(input("Enter the cost (in cents):\n"))
if C:
    
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    dep=deposit
    
    while dep<C:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        dep=deposit+dep
        
    change=dep-C
    
    if change>=1:
        print("Your change is:")
    out1=change//100
    
    if out1>0:
        print(out1,"x $1")
        change=change- (out1*100)
    out2=change//25
    
    if out2>0:
        print(out2,"x 25c")
        change=change- (out2*25)
    out3=change//10
    
    if out3>0:
        print(out3,"x 10c")
        change=change- (out3*10)
    out4=change//5
    
    if out4>0:
        print(out4,"x 5c")
        change=change- (out4*5)
    out5=change//1
    
    if out5>0:
        print(out5,"x 20c")
        change=change- (out5*20)
    out6=change//1
    
    if out6>0:
        print(out6,"x 1c")
        change=change- (out6*1)
    #out7=change//5
    
    #if out7>0:
     #   print(out7,"x 5c")
        
        
#finish=input("")