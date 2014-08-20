cost = eval(input("Enter the cost (in cents):\n"))
if cost>0:
    dep = eval(input("Deposit a coin or note (in cents):\n"))
    while dep < cost:
        depmore = eval(input("Deposit a coin or note (in cents):\n"))
        dep += depmore
    result = dep - cost
    final = "Your change is:\n"
    if result!=0:
        if result >= 100:
            ones = result//100
            result -= ones*100
            final += str(ones)+" x $1\n"
        if result >= 25:
            tf = result//25
            result -= tf*25
            final += str(tf)+" x 25c\n"
        if result >= 10:
            tens = result//10
            result -=tens*10
            final += str(tens)+" x 10c\n"
        if result >= 5:
            fives = result//5
            result -=fives*5 
            final += str(fives)+" x 5c\n"
        if result >= 1:
            cent = result//1
            result -=cent
            final += str(cent)+" x 1c\n"    
    else:
        final=""
    print(final)