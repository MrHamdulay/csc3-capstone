#change calculator
#Aniq Hartle
#16-04-2014

#get cost from user
cost = eval(input("Enter the cost (in cents):\n"))
paid = 0

if cost>0:    
    #get payment until exeeded or = to cost
    while cost>paid:
        paid+=eval(input("Deposit a coin or note (in cents):\n"))
    #work out the difference in paid vs cost
        diff = paid - cost     
    if diff>0:    
        #allocate change and subtract from the difference to calculate
        print("Your change is:")
        if (diff)//100!=0:
            print(diff//100, "x $1")
            diff-=(100*(diff//100))
        if diff//25!=0:
            print(diff//25, "x 25c")
            diff-=(25*(diff//25))
        if diff//10!=0:
            print(diff//10, "x 10c")
            diff-=(10*(diff//10))    
        if diff//5!=0:
            print(diff//5, "x 5c")
            diff-=(5*(diff//5))
        if diff//1!=0:
            print(diff//1, "x 1c")
            diff-=(1*(diff//1))    