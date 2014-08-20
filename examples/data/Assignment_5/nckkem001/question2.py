"""Program to simulate a change-providing vending machine.
Kemeshan Naicker
16 April 2014"""

def Vending_Machine():
#Get user to input cost.
    cost = eval(input("Enter the cost (in cents):\n"))
#Get user to deposit coins until deposited amount > cost.
    #Set initial deposited amount to 0.
    if cost != 0:
        coins = 0
        while coins<cost:
            newcoin=eval(input("Deposit a coin or note (in cents): \n"))
            coins+=newcoin
        #Oustanding amount set to variable "AM"
        AM = coins - cost
        #Set change as an empty list
        change=[]
        #Set if statements such that denominations are only listed if AM > denomination
        #Append all denominations used to the list
        if AM != 0:       
            
            if AM >= 100:
                one_d = str(AM//100)
                AM %= 100
                change.append(one_d+" x $1")
    
            if AM >= 25:
                c25 = str(AM//25)
                AM %= 25
                change.append(c25+" x 25c")
        
            if AM >= 10:
                c10 = str(AM//10)
                AM %= 10
                change.append(c10+" x 10c")       
    
            if AM >= 5:
                c5 = str(AM//5)
                AM %= 5
                change.append(c5+" x 5c")     
            if AM > 0:
                change.append(str(AM)+" x 1c")
            #Join the list with new lines and print change given
            print("Your change is:\n","\n".join(change),sep="")
    
Vending_Machine()