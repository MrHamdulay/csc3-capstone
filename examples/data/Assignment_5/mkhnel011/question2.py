"""program to calculaate the channge, a certain amount of money"""
# nelisile mkhwebane
# 14/04/2014
# assignment 5

# get the input 
cost=eval(input("Enter the cost (in cents):\n"))

#initialize the total amount

totalamount=0

#Check if the amount entered matches the cost

while totalamount < cost:
        more= eval(input("Deposit a coin or note (in cents):\n"))
        totalamount += more
        if more > cost :
                break
# calculating your change

change= totalamount-cost

#if len(str(change))== 3 or len(str(change))==2 or len(str(change))== 1:
        
dollars=change//100
twofive=(change%100)//25
tens=((change%100)%25)//10
y=(((change%100)%25)%10)//5
z=((((change%100)%25)%10)%5)//1
if dollars!=0 or twofive!=0 or tens!=0 or z!=0 or y!=0:
        print("Your change is:")
        if dollars!=0:
                print ( dollars, " x $1", sep="")
        if twofive!=0:
                print( twofive, " x 25c",sep="")
        if tens !=0:
                print( tens, " x 10c", sep="")
        if y != 0:
                print(y, " x 5c", sep="")
        if z !=0:
                print(z, " x 1c", sep ="")

#if len(str(change))==1:
        #if change == 1:
                #print("Your change is:")
                #print("1", " x ", change,"$",sep="")
        #elif change>1:
                #print("Your change is:")
                #print(change//1, " x 1$",sep="")
            
#elif len(str(change))==2:
        #u = str(change)[1]
        #t = str(change)[0]
        #h = 0
        #if change==10:
                #print("Your change is:")
                #print("1 x ",change,"$",sep="")
        #elif change == 25:
                #print("Your change is:")
                #print("1 x ", change, "c",sep="")
        #elif change>10:
                #if change%10 == 0:
                        #print("Your change is:")
                        #print(change//10, " x 10c", sep="")
        #elif change%25==0:
                #print("Your change is:")
                #print(change//25," x 25c", sep="")
        #elif change%10!=0:
                #print("Your change is:")
                #print(t, " x 10c",sep="")
                #if u == 1:
                        #print("1 x ",u, "c", sep="")
                #elif eval(u)>1:
                        #print(eval(u)//1, " x 1c", sep="")
                #elif eval(u)== 5:
                        #print("1 x ", u, "c", sep="")



    # check if the entered amount meets equals the required amount
# the change is equal po the difference in entered amount and required amount
