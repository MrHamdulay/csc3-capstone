price=eval(input("Enter the cost (in cents):\n"))

def input_coin():
    global price
    global x
    coin=eval(input("Deposit a coin or note (in cents):\n"))
    price=price-coin
    if price>0:
        input_coin()
    elif price==0:
        program="cancel"
        # donothing
    else:
        x=price
        change()

def change():
    global x
    x*=-1
    rem=x%100
    dollar=(x-rem)//100
    x=x-(dollar*100)
    rem2=x%25
    twenty5=(x-rem2)//25
    x=x-(twenty5*25)
    rem3=x%10
    tens=(x-rem3)//10
    x=x-(tens*10)
    rem4=x%5
    fives=(x-rem4)//5
    x=x-(fives*5)
    penny=x
    print("Your change is:")
    if dollar!=0:
        print(dollar, "x $1")
    if twenty5!=0:
        print(twenty5, "x 25c")
    if tens!=0:
        print(tens, "x 10c")
    if fives!=0:
        print(fives, "x 5c")
    if penny!=0:
        print(penny, "x 1c")

if price>0:
    input_coin()
