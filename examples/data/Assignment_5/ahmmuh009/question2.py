"""Muhammad Ahmad
AHMMUH009
17 April 2014"""


def change():
    cost=int(input("Enter the cost (in cents):\n"))         #input cost
    deposits=0
    while cost > deposits :             #Loops until enough money is entered
        dep=int(input("Deposit a coin or note (in cents):\n"))
        deposits+=dep
    change=deposits-cost
    list_2=["25c","10c","5c","1c"]          #allowed change we will use
    list_1=[]
    num=100
    while change>0:             #loops as long as more change is required
        num=change//100             #calculates the change in dollars
        change=change-(num*int(100))        
        list_1.append(str(num)+" "+"x"+" "+"$1")        #adds the change to the empty string
        for k in list_2:        
            num=change//int(k[0:len(k)-1])
            change=change-(num*int(k[0:len(k)-1]))
            list_1.append(str(num)+" "+"x"+" "+k)
        print("Your change is:")
        for i in list_1:
            if i[0]!="0":
                print(i)
            
change()