"""Naveet Baitchu
Change programme
17/04/14"""



def main():
    a=0
    Dollar=0
    Quarter=0
    TenC=0
    FiveC=0
    OneC=0
    x=eval(input("Enter the cost (in cents): \n"))
    
    while a<x:
        y=eval(input("Deposit a coin or note (in cents): \n"))
        a=a+y
    z=a-x #z=change
    
   
    while z>=100:
        z=z-100
        Dollar=Dollar+1
        
    while z>=25:
        z=z-25
        Quarter=Quarter+1
    
    while z>=10:
        z=z-10
        TenC=TenC+1
    
    while z>=5:
        z=z-5
        FiveC=FiveC+1
    
    while z>=1:
        z=z-1
        OneC=OneC+1

    if z==0 and x>0:
        
        print("Your change is: ")
        if Dollar>0:
            print(Dollar,"x $1")
        if Quarter>0:
            print(Quarter,"x 25c")
        if TenC>0:
            print(TenC,"x 10c")
        if FiveC>0:
            print(FiveC,"x 5c")
        if OneC>0:
            print(OneC,"x 1c")
    
main()