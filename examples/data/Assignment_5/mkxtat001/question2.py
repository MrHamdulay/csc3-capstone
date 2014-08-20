#Tato Moaki MKXTAT001
#Program to simulate vending machine
#Assignment5 question2

def main():
    
    cost = int(input("Enter the cost (in cents):\n"))#accept integer deposits 
    totalDeposit = 0
    
    while(totalDeposit < cost):#loop until the totaldeposit is at least greater the cost
        deposit = int(input("Deposit a coin or note (in cents):\n"))
        totalDeposit += deposit
        
    totalChange = totalDeposit - cost
    if(totalChange > 0):
        print("Your change is:")
    
    for i in (100, 25, 10, 1):
        if(totalChange % i != totalChange):# if i does divide totalChange else next value  of i
            divisor = totalChange // i #integer division  
            remainder = (totalChange - (divisor * i))
            if(i == 100):
                print(str(divisor)+" x "+"$1")
            else:
                print(str(divisor)+" x",str(i)+"c")
            totalChange = remainder

if __name__=="__main__":
    main()
        