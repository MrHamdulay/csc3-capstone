#Calculating change
#Author: Gordon Skhosana
#Date: 12/04/2014
   
def vending_machine():
    cost=eval(input("Enter the cost (in cents):\n"))
    if cost!=0:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))    
        while deposit<cost:
            deposited=eval(input("Deposit a coin or note (in cents):\n"))
            deposit+=deposited
        change=deposit-cost
        def change_calc():   
            no_of_100_cents=change//100
            no_of_25_cents=(change-(no_of_100_cents)*100)//25
            no_of_10_cents=(change-(no_of_100_cents)*100-(no_of_25_cents)*25)//10
            no_of_5_cents=(change-(no_of_100_cents)*100-(no_of_25_cents)*25-(no_of_10_cents)*10)//5
            no_of_1_cents=(change-(no_of_100_cents)*100-(no_of_25_cents)*25-(no_of_10_cents)*10-(no_of_5_cents)*5)//1
            if no_of_100_cents!=0 or no_of_25_cents!=0 or no_of_5_cents!=0 or no_of_1_cents!=0:
                print("Your change is:")
                if no_of_100_cents!=0:
                    print(no_of_100_cents," x"," $1",sep="")
                if no_of_25_cents!=0:
                    print(no_of_25_cents," x"," 25c",sep="")
                if no_of_10_cents!=0:
                    print(no_of_10_cents," x"," 10c",sep="")
                if no_of_5_cents!=0:
                    print(no_of_5_cents," x"," 5c",sep="")
                if no_of_1_cents!=0:
                    print(no_of_1_cents," x"," 1c",sep="")
        #Different scenarios that cause different change denominations
        if change%100==0:
            change_calc()
        elif change%25==0:
            change_calc()
        elif change%10==0:
            change_calc()
        elif change%5==0:
            change_calc()
        else:
            change_calc()
vending_machine()