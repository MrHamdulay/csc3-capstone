"""vending machine program that asks for money until the required price is paid
   and then gives change, if any
   nitisha makanjee
   16 april 2014"""


# adding money until the money paid is equal to the cost
# storing the excess, if any
def payment(cost):
    limit=0
    payment=0
    while limit<=cost:
        if limit!=cost:
            payment=eval(input("Deposit a coin or note (in cents):\n"))
            limit+=payment
        else:
            break
    # print(limit) proves that the full amount being paid is being recorded
    change=limit-cost
    return change
    #print("Your change is", change)
          
# working out the change needed
# with the change that you get, you have to convert the cents into change using
# the largest numbers in the list
# the change must be equal to the cents
def change(change):
    list1= [100, 25, 10, 5, 1] # let's work with everything in cents
    count1, count2, count3, count4, count5=0, 0, 0, 0, 0
    while change!=0:
        print("Your change is:")
        for i in list1:
            if i>change:
                continue
            else:
                if i==100:
                    while i<=change:
                        change-=i
                        #print("change remaining =", change)
                        count1+=1
                        #print("Count1 multiplier is", count1)
                    print(count1, "x $1")
                elif i==25:
                    while i<=change:
                        change-=i
                        #print("change remaining =", change)
                        count2+=1   
                        #print("Count2 multiplier is", count2)
                    print(count2, "x 25c")
                elif i==10:
                    while i<=change:
                        change-=i
                        #print("change remaining =", change)
                        count3+=1
                        #print("Count3 multiplier is", count3)
                    print(count3, "x 10c")
                elif i==5:
                    while i<=change:
                        change-=i
                        #print("change remaining =", change)
                        count4+=1  
                        #print("Count4 multiplier is", count4)
                    print(count4, "x 5c")
                elif i==1:
                    while i<=change:
                        change-=i
                        #print("change remaining =", change)
                        count5+=1          
                        #print("Count5 multiplier is", count5)
                    print(count5, "x 1c")
        
# inputing the cost
cost=eval(input("Enter the cost (in cents):\n"))
change(payment(cost))