def vending():
    """simulate a vending machine, taking user input and returning remainder."""
    t= eval(input("Enter the cost (in cents):\n"))
    x= 0
    while x<t:
        x+= eval(input("Deposit a coin or note (in cents):\n"))
    if x>t:
        sum=x-t
        if sum!=0:
            print("Your change is:")
        money=sum//100
        if money!= 0:
            print(money,'x $1')
        b= (sum -money*100)//25
        if b!= 0:
            print(b,'x 25c')
            c= (sum -money*100 -b*25)//10
        if c!= 0:
            print(c,'x 10c')
        d= (sum -money*100 - b*25 - c*10)//5
        if d!= 0:
            print(d,'x 5c')
        e= (sum -money*100 - b*25 - c*10 -d*5)//1
        if e!= 0:
            print(e,'x 1c')

vending()