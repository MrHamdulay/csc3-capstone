# program to simulate a vending machine and calculate change based on the amount paid
#Raeesa Behardien
#17 April 2014

def main():
    cost = eval(input("Enter the cost (in cents):" '\n'))
    deposit = 0
    while deposit<cost:
        amt_deposit = eval(input("Deposit a coin or note (in cents):" '\n'))
        deposit+=amt_deposit
    change=deposit-cost
    #change = cost - deposit
    new_change=change

    #while change != sum_change:
    if change != 0:
        print("Your change is:")
    if change >= 100:
        print(change//100, "x $1")
        new_change = change%100
    if new_change >= 25:
        print(new_change//25, "x 25c")
        new_change = new_change%25
        #sum_change+= new_change
    if new_change >= 10:
        print(new_change//10,"x 10c")
        new_change = new_change%10            
        #sum_change+= new_change
    if new_change >= 5:
        print(new_change//5, "x 5c")
        new_change = new_change%5
        #sum_change+= new_change
    if new_change != 0:
        print(new_change//1, "x 1c")
            #new_change = new_change%1            
            #sum_change+= new_change  
            
    #print("Your change is:")
    #if a != 0:
        #print(a,"x $1")
    #elif b != 0:    
        #print(b,"x 25c")
    #elif c != 0:    
        #print(c,"x 10c")
    #elif d != 0:    
        #print(d,"x 5c")    
    #elif e != 0:    
        #print(e,"x 1c")
    #else:
        #print("0c")
main()