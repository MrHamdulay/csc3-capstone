cost= eval(input("Enter the cost (in cents):"'\n'))
if cost==0:
    print("")
else:
    deposit= eval(input("Deposit a coin or note (in cents):"'\n'))
    while deposit<cost:
        deposit1= eval(input("Deposit a coin or note (in cents):"'\n'))
        deposit= deposit + deposit1
    if deposit>cost:
        change= deposit-cost
        d=(change)//100
        tfc=(change-d*100)//25
        tc=(change-d*100-tfc*25)//10
        fc=(change-d*100-tfc*25-tc*10)//5
        oc=(change-d*100-tfc*25-tc*10-fc*5)//1
        print("Your change is:")
        if d!=0:
            print(d,"x $1")
        if tfc!=0:
            print(tfc,"x 25c")
        if tc!=0:
            print(tc,"x 10c")
        if fc!=0:
            print(fc,"x 5c")
        if oc!=0:
            print(oc,"x 1c")
        
        