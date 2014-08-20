"""As.5, Q.2 - vending machine and change
emma jordi
15 april 2014"""

#get cost
cost= eval(input("Enter the cost (in cents):\n"))
#add money until money >= cost

total_deposited=0
money=0

if cost!=0:
    
    while total_deposited < cost:
        money=eval(input("Deposit a coin or note (in cents):\n"))
        total_deposited = total_deposited + money
        #CHECKED

        hundreds=0
        t_fives=0
        tens=0
        fives=0
        ones=0
        #if total_deposited > cost, calculate change amount
        if total_deposited > cost:
            change= total_deposited - cost #CHECKED
    
       
            #divide change amount into coins        
            while change>0:
                hundreds= change//100
                change= change%100
                t_fives= change//25
                change = change%25
                tens= change//10
                change= change%10
                fives= change//5
                change= change%5
                ones=change//1
                change=change%1
                
                #print change if more than zero
                print("Your change is:")
                if hundreds>0:
                    print(hundreds, "x $1")
    
                if t_fives>0:
                    print(t_fives, "x 25c")

                if tens>0:
                    print(tens, "x 10c")
    
                if fives>0:
                    print(fives, "x 5c")
                                
                if ones>0:
                    print(ones, "x 1c")
                        
                                  

