'''program to simulate a vending machine
Wandile Khowa
15-04-2014
'''
price = eval(input("Enter the cost (in cents): \n")) 
if price == 0:
    print()
else:
    paid1 = eval(input("Deposit a coin or note (in cents): \n"))   
    while paid1-price < 0:
        paid2 = eval(input("Deposit a coin or note (in cents): \n"))
        paid1 = paid1+paid2

    if paid1-price > 0: #calcultes how much change is given in dollars
        change = paid1-price
        dollars = change//100
        line1 = 0
        if dollars != 0:
            line1 = dollars*1
        else:
            line1 = 0
        
        cents = change-(dollars*100)
        i = 0
        line2 = 0
        while cents-25 >= 0: #calculates how much change is given in 25cents
            cents -= 25 
            i = i+1
            
        line2 = i*25
        cents1 = cents 
        j = 0
        line3 = 0
        while cents1 -10 >= 0: #calculates how much change is given in 10cents
            cents1 -= 10
            j = j+1
        
        line3 = j*10
        cents2 = cents1
        k = 0
        line4 = 0
        while cents2 -5 >= 0: #calculates how much change is given in 5cents
            cents2 -= 10
            k = k+1
        
        line4 = k*5
        cents3 = cents2
        l = 0
        line5 = 0
        while cents3 - 1 >= 0: #calculates how much change is given in 1cent
            cents3-=1
            l = l+1
        
        line5 = l*1
        print("Your change is:") #prints out the total change in correct format
        if line1 != 0: #checks if there is any change given in dollars
            print(dollars, "x $1")
        if line2 != 0: #checks if there is any change given in 25cents
            print(i, "x 25c")
        if line3 != 0: #checks if there is any change given in 10cents
            print(j, "x 10c")
        if line4 != 0: #checks if there is any change given in 5cents
            print(k, "x 5c")
        if line5 != 0: #checks if there is any change given in 1cents
            print(l, "x 1c")
        
    
        
    
        
        

        
        
    