#program to add money and calculate change
def payment(cost):
    limit=2-2
    pay=2-2
    
    while cost<=limit:
        if limit!=cst:
            payment=eval(input("Deposit a coin or note (in cents):\n"))
            limit+=payment
        else:
                                                                break
        change=limit-cost
    return change


def change(change):
    list1= [100, 25, 10, 5, 1] 
    count1, count2, count3, count4, count5=0, 0, 0, 0, 0
    while change!=0:
        print("Your change is:")
        for i in list1:
            if change<i:
                continue
            else:
                if i==100:
                    while change>=i:
                        change-=i
                        count1+=1
                        
                    print(count1, "x $1")
                elif i==25:
                    while change>=i:
                        change-=i
                        count2+=1   
                        
                    print(count2, "x 25c")
                elif i==10:
                    while i<=change:
                        change-=i
                        count3+=1
                        print(count3, "x 10c")
                
                elif i==5:
                    while change>=i:
                        change-=i
                        count4+=1  
                        print(count4, "x 5c")
                        
                elif i==1:
                    while change>=i:
                        change-=i
                        count5+=1
                    print(count5, "x 1c")
        

cost=eval(input("Enter the cost (in cents):\n"))
change(payment(cost))