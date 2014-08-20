"""program to simulate a vending machine
thushar hariparsad
15 april 2014"""


cost=eval(input("Enter the cost (in cents):\n"))
#deposit = eval(input("Deposit a coin or note (in cents):\n"))
total=0
while total < cost and cost!=0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    total=total+deposit 
if total > cost:
    change=total-cost
    print("Your change is:")
    one_dollar=0
    quarter=0
    tencents=0
    fivecents=0
    onecent=0
    while change > 0:
        if change/100 >=1:
            one_dollar=change//100
            change-=(one_dollar*100)
        if change/25 >=1:
            quarter=change//25
            change-=(quarter*25)
        if change/10 >=1:
            tencents=change//10
            change-=(tencents*10)
        if change/5 >=1:
            fivecents=change//5
            change-=(fivecents*5)
        if change/1 >=1:
            onecent=change//1
            change-=onecent
        if one_dollar:
            print(one_dollar,"x $1")
        if quarter:
            print(quarter,"x 25c")
        if tencents:
            print(tencents,"x 10c")
        if fivecents:
            print(fivecents,"x 5c")
        if onecent:
            print(onecent,"x 1c")
        
     