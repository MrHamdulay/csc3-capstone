def vending_machine():
    cost=eval(input("Enter the cost (in cents):\n"))
    initial=0    
    while True:
        if cost==0: break
        
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        initial+=deposit
        if initial>cost:
            total_paid=initial
            difference=total_paid-cost
            dollars=difference/100
            dollar=int(dollars)
            Dollars=dollars-dollar
            cents=int(Dollars*100)
            a=difference%100
            
            if a==0:   #criteria 1: change divisible by 100 (can give change in $1 only)
                x=difference//100
                print("Your change is:")
                print(x,"x", "$1")
                
            elif a!=0:  #criteria 2: change not divisible by 100, need other coins
                check=difference%100
                if check==50:  #criteria 2a :after giving $1, have to give 50c, i.e, two 25c
                    x=difference//100
                    print("Your change is:")
                    print(x,"x","$1")
                    print("2 x 25c")
                else:                  #criteria 2b:
                    check2=difference%100
                    if check2==25:
                        x=difference//100
                        remaining=difference-x*100
                        y=remaining//25                        
                        print("Your change is:")
                        print(x,"x","$1")
                        print(y,"x","25c")
                        
                    else:
                        check3=difference%10
                        if check3==5:
                            
                            if difference<=99:
                                x=difference//25
                                remaining=difference-x*25
                                y=remaining//10                           
                                print("Your change is:")
                                print(x,"x","25c")
                                print(y,"x","10c")
                            else:
                                x=difference//100
                                remaining=difference-x*100
                                y=remaining//25
                                remaining2=remaining-y*25
                                z=remaining2//10
                                print("Your change is:")
                                print(x,"x","$1")
                                print(y,"x","25c")
                                print(z,"x","10c")                                
                        else:
                            x=difference//100
                            remaining=difference-x*100
                            y=remaining//25
                            remaining2=remaining-y*25
                            z=remaining2//10
                            print("Your change is:")
                            print(x,"x","$1")
                            print(y,"x","25c")
                            print(z,"x","10c")
                    
                
            break
        elif initial==cost: break 
vending_machine()