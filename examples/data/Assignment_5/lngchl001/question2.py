# vending machine simulator
#by Chloe Longmore
# 15 April 2014

cost=eval(input("Enter the cost (in cents):\n"))

def payment():
    paid=0
    #add more money to pay with
    while cost>paid:
        paying=eval(input("Deposit a coin or note (in cents):\n"))
        paid+=paying
    #when cost=amount paid
    if paid==cost:
        print("")
    if paid>cost:
        print("Your change is:")
        extra=paid-cost
       # calculating change
        if extra>100:
            dollar=0
            two_five_c=0
            ten_c=0
            five_c=0
            one_c=0
            #calculating dollar amount
            for i in range(int(extra/100)):
                dollar+=1
            if dollar>=1:
                print(dollar,"x $1")
            #calculating 25c amount
            change2=extra%100
            for i in range(int(change2/25)):
                two_five_c+=1
            if two_five_c>=1:
                print(two_five_c,"x 25c")
                #calculating 10c amount
            change3=change2%25
            for i in range(int(change3/10)):
                ten_c+=1
            if ten_c>=1:
                print(ten_c,"x 10c")
                #calculating 5c amount
            change4=change3%10
            for i in range(int(change4/5)):
                five_c+=1
            if five_c>=1:
                print(five_c,"x 5c")
                #calculating 1c amount
            change5=change4%5
            for i in range(int(change5/1)):
                one_c+=1
            if one_c>=1:
                print(one_c,"x 1c")
                
payment()
    
