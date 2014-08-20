"""Program to simulate vending machine and calculate change based on the amount paid"""
#vuyolwethu nkosi
#15 april 2014

def vending_machine(): #program definition
    cost = eval(input("Enter the cost (in cents):\n")) #user input
    if cost>0: #if what the user wants has a cost they must enter money into the machine
        dep = eval(input("Deposit a coin or note (in cents):\n"))
        while cost>dep: #if what the user deposited into the machine is less than the cost, more money must be put in
                dep = dep+eval(input("Deposit a coin or note (in cents):\n"))
                #dep = dep+dep #keep adding to what the user already has put in
        chnge = dep-cost #change to the user 
        #changing notes and coins to cents
        change_dollar = chnge//100
        rem = chnge%100 
        m = rem//25 
        rem_2 = rem%25
        n = rem_2//10
        rem_3 = rem_2%10
        o = rem_3//1
        
        if dep>cost: #if user has put in more money into the machine than what item costs execute this portion
                if chnge>=100: #if balance or rather change is greater than 100 cents, which is a dollar
                        if rem==0: #change in notes has no remainder
                                print("Your change is:\n",change_dollar," x $1",sep="")
                        elif rem!=0 and rem_2==0: #if notes remainder and 25c has no remainder
                                print("Your change is:\n",change_dollar," x $1\n",m," x 25c",sep="")
                        elif rem!=0 and rem_2!=0 and rem_3==0: #if notes and 25c have remainder, theres 10cents 
                                print("Your change is:\n",change_dollar," x $1\n",m," x 25c\n",n," x 10c",sep="")
                        elif rem!=0 and rem_2!=0 and rem_3!=0: 
                                print("Your change is:\n",change_dollar," x $1\n",m," x 25c\n",n," x 10c\n",o," x 1c",sep="")
                elif chnge>=25: #if theres no notes but coins
                        if rem!=0 and rem_2==0: #only 25cents
                                print("Your change is:\n",m," x 25c",sep="")
                        elif rem!=0 and rem_2!=0 and rem_3==0: #only 25c and 10c
                                print("Your change is:\n",m," x 25c\n",n," x 10c",sep="")
                        elif rem!=0 and rem_2!=0 and rem_3!=0: #only 25, 10 and 1 cent
                                print("Your change is:\n",m," x 25c\n",n," x 10c\n",o," x 1c",sep='') 
                elif chnge>=10: #no 25c
                        if rem!=0 and rem_2!=0 and rem_3==0:
                                print("Your change is:\n",n," x 10c",sep="")
                        elif rem!=0 and rem_2!=0 and rem_3!=0:
                                print("Your change is:\n",n," x 10c\n",o," x 1c",sep="") 
                elif chnge>=1: #no 10c
                        if rem!=0 and rem_2!=0 and rem_3!=0:
                                print("Your change is:\n",o," x 1c",sep="") 
                        else: #no change
                                ()
        else:
                ()
vending_machine()