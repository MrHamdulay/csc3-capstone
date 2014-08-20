"""Change working programme
#Rama Raphalalani
#15-04-2014"""

x = eval(input("Enter the cost (in cents):\n"))
if x>0:
    y = eval(input("Deposit a coin or note (in cents):\n"))
    while x>y:
            y = y + eval(input("Deposit a coin or note (in cents):\n"))
            #y = y+y
    change = y-x
    #calculates the different forms of change for the coins the machine has
    z = change//100
    remainder = change%100
    a = remainder//25
    remainder2 = remainder%25
    b = remainder2//10
    remainder3 = remainder2%10
    c = remainder3//1
    
    #process for checking which change to give according to the various amounts of change
    if y>x:
            if change>=100:
                    if remainder==0:
                            print("Your change is:\n",z," x $1",sep='')
                    elif remainder!=0 and remainder2==0:
                            print("Your change is:\n",z," x $1\n",a," x 25c",sep='')
                    elif remainder!=0 and remainder2!=0 and remainder3==0:
                            print("Your change is:\n",z," x $1\n",a," x 25c\n",b," x 10c",sep='')
                    elif remainder!=0 and remainder2!=0 and remainder3!=0:
                            print("Your change is:\n",z," x $1\n",a," x 25c\n",b," x 10c\n",c," x 1c",sep='')
            elif change>=25:
                    if remainder!=0 and remainder2==0:
                            print("Your change is:\n",a," x 25c",sep='')
                    elif remainder!=0 and remainder2!=0 and remainder3==0:
                            print("Your change is:\n",a," x 25c\n",b," x 10c",sep='')
                    elif remainder!=0 and remainder2!=0 and remainder3!=0:
                            print("Your change is:\n",a," x 25c\n",b," x 10c\n",c," x 1c",sep='') 
            elif change>=10:
                    if remainder!=0 and remainder2!=0 and remainder3==0:
                            print("Your change is:\n",b," x 10c",sep='')
                    elif remainder!=0 and remainder2!=0 and remainder3!=0:
                            print("Your change is:\n",b," x 10c\n",c," x 1c",sep='') 
            elif change>=1:
                    if remainder!=0 and remainder2!=0 and remainder3!=0:
                            print("Your change is:\n",c," x 1c",sep='') 
                    else:
                            ()
    else:
            ()
    