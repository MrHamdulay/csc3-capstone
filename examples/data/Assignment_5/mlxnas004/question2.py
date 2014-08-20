def vendingmachine():
    paid = 0
    total = eval(input("Enter the cost (in cents):\n"))
    while paid < total:
        paid+=eval(input("Deposit a coin or note (in cents):\n"))
        
    if paid > total:
        change = paid-total
        if change >= 100:
            change1 = change//100
            sparechange=change%100
        else:
            sparechange=change
            change1=0
        if sparechange >= 25:
            if change >=100:
                change2=sparechange//25
                sparechange2=sparechange%25
            else:
                change2= change//25
                sparechange2=change%25
                
        else:
            sparechange2=sparechange
            change2 = 0
            
        if sparechange2>= 10:
            
            if change >= 25:
                change3=sparechange2//10
                sparechange3=sparechange2%10
            else:
                change3=change//10
                sparechange3=change%10
        else:
            sparechange3=sparechange2
            change3=0
        
        if sparechange3>=5:
            if change >= 10:
                change4=sparechange3//5
                sparechange4=sparechange3%5
            else:
                change4=change//5
                sparechange4=change%5
        else:
            sparechange4=sparechange3
            change4 =0
        if sparechange4>=1:
            if change >=5:
                change5=sparechange4//1
            else:
                change5=change//1
        else:
            change5 = 0
        if change > 0:
            print("Your change is:")
        if change1 != 0:
            print (change1,"x $1")
        if change2 != 0:
            print (change2,"x 25c")
        if change3 != 0:
            print (change3,"x 10c")        
        if change4 != 0:
            print (change4,"x 5c") 
        if change5 != 0:
            print (change5,"x 1c")        
            
vendingmachine()
                