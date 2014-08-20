"""Program to simulate a vending machine and calculate change based on the amount paid.
Elizabeth Cilliers
14/04/2014"""

def main():
    #ask user to input the cost of the good.
    cost=eval(input("Enter the cost (in cents):\n"))
   
    #if the cost of the good is 0 then do no execute any following statments.
    while cost==0:
        break
   
    #if cost is not zero then ask user to input the value of their deposit.
    else:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))        
    
    #if the deposit is not enough to meet the cost them ask them to deposit more.    
        while deposit< cost:
            deposit2=eval(input("Deposit a coin or note (in cents):\n"))
            deposit=deposit + deposit2 #add new deposit to original deposit to get the total amout deposited.
        
        while deposit==cost:
            break
        
        else:#Work out how much change.
            change=deposit-cost
            
            dollars=change//100 #deposit minus cost is the total amount to be given in change. divide by 100 to get how many dollars can be given.
            
            change=change%100
            
            twentyfives=change//25 #divide remainder of previous equation to get how many 25cents can be given.
            
            change=change%25
            
            tens=change//10 #divide remainder of previous equation to get how many 10cents can be given.
            
            change=change%10
            
            onecents=change%10 #divide remainder of previous equation to get how many 1cents can be given.
            
            #print out the amount of change to be given.
            print("Your change is:")
    
            if dollars>0:
                print(dollars,"x $1")
    
            if twentyfives>0:
                print(twentyfives,"x 25c")
    
            if tens>0:
                print(tens,"x 10c")

            if onecents>0:
                print(onecents,"x 1c")          
       
main()