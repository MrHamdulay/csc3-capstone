cost = eval(input("Enter the cost (in cents):\n"))
minus =0
rem = cost
while rem > 0:
    depo = eval(input("Deposit a coin or note (in cents):\n"))
    minus+=depo
    rem -= depo
if rem == 0:
    print()
else:
    tdol = 0
    t25 =0
    t10 =0
    t5=0
    t1 = 0
    rem*=-1
    r = (rem%100)
    tdol = (rem-r)//100
    r2 = r%25
    t25 = (r-r2)//25
    r3 = r2%10
    t10 = (r2-r3)//10   
    r4 = r3%5
    t5 = (r3-r4)//5
    r5 = r4%1
    t1 = (r4-r5)//1    
    print("Your change is:")
    if tdol > 0:
        print(tdol,"x","$1")
    if t25 > 0:
        print(t25,"x","25c")
    if t10 > 0:
        print(t10,"x","10c")
    if t5 > 0:
        print(t5,"x","5c")
    if t1 > 0:
        print(t1,"x","1c")    






# 1c, 5c, 10c, 25c, $1