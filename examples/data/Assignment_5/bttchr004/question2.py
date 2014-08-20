#program to work out change
#chris betteridge
#14 April 2014

cost = eval(input("Enter the cost (in cents):\n"))
rem_cost = cost
while rem_cost > 0:
    amount_paid = eval(input("Deposit a coin or note (in cents):\n"))
    rem_cost = rem_cost - amount_paid
    if rem_cost <= -100:
        print("Your change is:")
        remcost_str = str(rem_cost*-1)
        LengthOfChangeString = len(remcost_str)
        units = eval(remcost_str[0:LengthOfChangeString-2])
        units_change = (units//units)
        cents = eval(remcost_str[LengthOfChangeString-2:])
        cents1 = cents//25
        cents2 = (cents - cents1*25)//10
        cents3 = (cents - cents1*25 - cents2*10)//5
        cents4 = (cents - cents1*25 - cents2*10 - cents3*5)
        print(units," x ","$",units_change,sep='')
        if cents1 > 0:
            print(cents1,"x 25c")
        if cents2 > 0:
            print(cents2,"x 10c")
        if cents3 > 0:
            print(cents3,"x 5c")
        if cents4 > 0:
            print(cents4,"x 1c")
    if rem_cost < 0 and rem_cost > -100:
        print("Your change is:")
        remcost_str = str(rem_cost*-1)
        cents = eval(remcost_str[:])
        cents1 = cents//25
        cents2 = (cents - cents1*25)//10
        cents3 = (cents - cents1*25 - cents2*10)//5
        cents4 = (cents - cents1*25 - cents2*10 - cents3*5)
        if cents1 > 0:
            print(cents1,"x 25c")
        if cents2 > 0:
            print(cents2,"x 10c")
        if cents3 > 0:
            print(cents3,"x 5c")
        if cents4 > 0:
            print(cents4,"x 1c")        