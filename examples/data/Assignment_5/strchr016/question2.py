"""Christopher Sterley
12/04/2014
Computer Science assignment"""

mon=eval(input("Enter the cost (in cents):\n"))
amo=0
while amo<mon:
    amo1=eval(input("Deposit a coin or note (in cents):\n"))
    amo=amo+amo1
else:
    change=amo-mon
    dollar=change//100
    cent25=(change%100)//25
    cent10=((change%100)%25)//10
    cent5=(((change%100)%25)%10)//5
    cent1=((((change%100)%25)%10)%5)
    if amo==mon or mon==0:
        print("")
    else:
        print("Your change is:")
        if dollar>0:
            print(dollar,"x","$1")
        if cent25>0:
            print(cent25,"x","25c")
        if cent10>0:
            print(cent10,"x","10c")
        if cent5>0:
            print(cent5,"x","5c")
        if cent1>0:
            print(cent1,"x","1c")