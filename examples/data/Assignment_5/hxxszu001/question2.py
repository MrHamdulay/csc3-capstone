cost = int(input("Enter the cost (in cents): \n"))
amount = 0
f = False

while(amount<cost):
    p= int(input("Deposit a coin or note (in cents): \n"))
    amount = amount + p

change = amount - cost
rand1 = 0
cent25 = 0
cent10 = 0
cent5 = 0
cent1= 0
mis = change
while(mis!=0):
    if(mis>=100):
        rand1=mis//100
        mis = mis-(rand1*100)
    elif(mis>=25):
        cent25=mis//25
        mis = mis-(cent25*25)
    elif(mis>=10):
        cent10=mis//10
        mis = mis-(cent10*10)
    elif(mis>=5):
        cent5=mis//5
        mis = mis-(cent5*5)    
    elif(mis>=1):
        cent1=mis//1 
        mis = mis-(cent1*1)
if(change!=0):
    print("Your change is:")
    if(rand1!=0):
        print(rand1,"x", "$1")
    if(cent25!=0):
        print(cent25, "x", "25c")
    if(cent10!=0):
        print(cent10, "x", "10c")
    if(cent5!=0):
        print(cent5, "x","5c")
    if(cent1!=0):
        print(cent1, "x", "1c")
   