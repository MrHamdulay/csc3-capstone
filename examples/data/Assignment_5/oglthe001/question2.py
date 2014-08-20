cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
while deposit < cost:
    deposit1=eval(input("Deposit a coin or note (in cents):\n"))
    deposit+=deposit1
    if deposit >= cost:
        break
change=deposit-cost
if change>0:
    print("Your change is:")
    ans=change/100
    if ans>0:
        ch100=change//100
        if ch100>0:
            print(ch100,"x $1")
        ch25=(change%100)//25
        if ch25>0 and change//100 != change/100:
            print(ch25,"x 25c")
        ans1=(change%100)%25
        ch10=ans1//10
        if ch10>0 and (change%100)//25 != (change%100)/25:
            print(ch10,"x 10c")
        ans2=(change%100)%25%10
        ch5=ans2//5
        if ch5>0 and (change%100)//25//10 != (change%100)/25/10:
            print(ch5,"x 5c")
        ans3=(change%100)%25%10%5
        ch1=ans3//1
        if ch1>0 and (change%100)//25//10//5 != (change%100)/25/10/5:
            print(ch1,"x 1c")