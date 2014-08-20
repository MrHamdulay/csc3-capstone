#Calculates the change of a payment
#Conor O'Sullivan
#15/4/2014

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    if cost != 0:
        dep = eval(input("Deposit a coin or note (in cents):\n"))
        while dep < cost:
            dep = dep + eval(input("Deposit a coin or note (in cents):\n"))
        ch = dep - cost
        if ch != 0:
            change(ch)
        

    
def change(ch):
    chList = [0,0,0,0,0]
    chAmt = ["$1",'25c','10c','5c','1c']
    while ch != 0:
        if (ch - 100) >= 0:
            ch -= 100
            chList[0] += 1
        elif (ch - 25) >= 0:
            ch -= 25
            chList[1] += 1
        elif (ch - 10) >= 0:
            ch -= 10
            chList[2] += 1   
        elif (ch-5)>= 0:
            ch -= 5
            chList[3] += 1
        elif (ch-1)>= 0:
            ch -= 1
            chList[4] += 1        
        
    print("Your change is:")
    for x in range(len(chList)):
        if chList[x] > 0:
            print(chList[x] , "x" , chAmt[x])

main()