# a program to simulate a vending machine and calculate change based on the amount paid
# mashau zwivhuya
# 12 / 04 /2014
def main():
    cost=eval(input("Enter the cost (in cents):\n"))
    money=0
    while money < cost:
        insert=eval(input("Deposit a coin or note (in cents):\n"))
        money=insert+money
    if money > cost:
        print("Your change is:")
        a=money-cost
        x=0
        if a>=100:
            x=a//100
            print(x,"x","$1")
        a=a-(100)*x
        if a>=25:
            x=a//25
            print(x,"x","25c")
        a=a-(25)*x
        if a>=10:
            x=a//10
            print(x,"x","10c")
        a=a-(10)*x
        if a>=5:
            x=a//5
            print(x,"x","5c")
        a=a-(5)*x        
        if a>=1:
            x=a//1
            print(x,"x","1c")
        a=a-(1)*x        
                                              
main()        