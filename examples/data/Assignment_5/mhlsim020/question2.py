"""A program to simulate a vending machine
Simlindile Mahlaba
17 April 2014"""

cost=eval(input("Enter the cost (in cents):\n")) 
if cost != 0:
    dep=eval(input("Deposit a coin or note (in cents):\n"))
    while dep<cost and cost != 0:
        dep+=eval(input("Deposit a coin or note (in cents):\n")) 
    while dep-cost!=0:
        print ("Your change is:")
        if (dep-cost>0):
            change1= (dep-cost)//100
            if change1>0:
                print(change1,"x $1")
        if dep-cost-(change1*100)==0:
            break
            
        if (dep-cost-(change1*100)>0):
            change2 = (dep-cost-(change1*100))//25
            if change2>0:
                print(change2,"x 25c")
        if dep-cost-(change1*100)-(change2*25)==0:
            break 
            
        if (dep-cost-(change1*100)-(change2*25)>0):
            change3 = (dep-cost-(change1*100)-(change2*25))//10
            if change3>0:
                print(change3,"x 10c")
        if dep-cost-(change1*100)-(change2*25)-(change3*10)==0:
            break   
            
        if (dep-cost-(change1*100)-(change2*25)-(change3*10)>0):
            change4 = (dep-cost-(change1*100)-(change2*25)-(change3*10))//5
            if change4>0:
                print(change4,"x 5c")
        if dep-cost-(change1*100)-(change2*25)-(change3*10)-(change4*5)==0:
            break 
            
        if (dep-cost-(change1*100)-(change2*25)-(change3*10)>0):
            change5 = (dep-cost-(change1*100)-(change2*25)-(change3*10)-(change4*5))//1
            if change5>0:
                print(change5,"x 1c")
        if dep-cost-(change1*100)-(change2*25)-(change3*10)-(change4*5)-(change5*1)==0:
            break
        break
       
        






