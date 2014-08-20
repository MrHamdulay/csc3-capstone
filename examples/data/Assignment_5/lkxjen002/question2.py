# A program simulating a vending machine
#Created by: Jenna Lake
#Date: 15/04/2014

def vend():
    dep=0
    cost=eval(input("Enter the cost (in cents):\n"))
    while dep<cost: #Checks if amount deposited has met the required amount(cost)
        dep+=eval(input("Deposit a coin or note (in cents):\n")) #if not it requests further deposits until greater or equal than cost
    x=dep-cost
    #program only prints the change of coin values of multiple greater than 0! (ie prints 2 x 10c, and does not print 0 x $1)
    if x>=100: #if total change (x) greater than 100c ($1) then follows this path
        d=x//100
        print("Your change is:")
        print(d,"x $1",sep=" ") #d is change in $1 notes
        e=x%(d*100)
        if e>=25:
            f=e//25
            print(f,"x 25c", sep=" ")#f is change in 25c coins
            g=e%(f*25)
            if g>=10:
                h=g//10
                print(h,"x 10c",sep=" ")#h is change in 10c coins
                i=g%(h*10)
                if i>=5:
                    j=i//5
                    print(j,"x 5c",sep=" ")#j is change in 5c coins
                    k=i%(5*j)
                    if k>1:
                        print(k,"x 1c",sep=" ")#k is change in 1c coins
                elif i>=1:
                    k=i
                    print(k,"x 1c",sep=" ")
            elif g>=5:
                i=g
                j=i//5
                print(j,"x 5c",sep=" ")
                k=i%(5*j)
                if k>=1:
                    print(k,"x 1c",sep=" ")
            elif g>=1:
                k=g
                print(k,"x 1c",sep=" ")
        elif e>=10:
            g=e
            h=g//10
            print(h,"x 10c",sep=" ")
            i=g%(h*10)
            if i>=5:
                j=i//5
                print(j,"x 5c",sep=" ")
                k=i%(5*j)
                if k>=1:
                    print(k,"x 1c",sep=" ")
        elif e>=5:
            i=e
            j=i//5
            print(j,"x 5c",sep=" ")
            k=i%(5*j)
            if k>=1:
                print(k,"x 1c",sep=" ")  
        elif e>=1:
            k=e
            print(k,"x 1c",sep=" ")
    elif x>=25:#if total change (x) is only greater than 25c ($1) then follows this path
        e=x
        f=e//25
        print("Your change is:")
        print(f,"x 25c", sep=" ")
        g=e%(f*25)
        if g>=10:
            h=g//10
            print(h,"x 10c",sep=" ")
            i=g%(h*10)
            if i>=5:
                j=i//5
                print(j,"x 5c",sep=" ")
                k=i%(5*j)
                print(k,"x 1c",sep=" ")
            elif i>=1:
                k=i
                print(k,"x 1c",sep=" ")
        elif g>=5:
            i=g
            j=i//5
            print(j,"x 5c",sep=" ")
            k=i%(5*j) 
            if k>=1:
                print(k,"x 1c",sep=" ")
    elif x>=10:#if total change (x) is only greater than 10c ($1) then follows this path
        g=x
        h=g//10
        print("Your change is:") # doesn't print "Your change is:" if there is no change, and only prints it once for a full set of change values
        print(h,"x 10c",sep=" ")
        i=g%(h*10)
        if i>=5:
            j=i//5
            print(j,"x 5c",sep=" ")
            k=i%(5*j)
            if k>=1:
                print(k,"x 1c",sep=" ")
        elif i>=1:
            k=i
            print(k,"x 1c",sep=" ")
    elif x>=5:#if total change (x) is only greater than 5c ($1) then follows this path
        i=x
        j=i//5
        print("Your change is:")
        print(j,"x 5c",sep=" ")
        k=i%(5*j)
        if k>=1:
            print(k,"x 1c",sep=" ")        
    elif x>=1: #if total change (x) is only greater than 1c ($1) then follows this path
        k=x
        print("Your change is:")
        print(k,"x 1c",sep=" ")
vend()