#Question 2 Assignment 5
#Konrad Hugo HGXKON001

price=eval(input("Enter the cost (in cents):\n"))

if price!=0: #Don't want to be prompted to deposit a coin if the product is free
    inserted=eval(input("Deposit a coin or note (in cents):\n"))
    total=inserted #You want the total to equal the first insertion initially, therefore allowing a correct sum
    while total<price: #While loop that runs until the total inserted is equal to or greater than the price 
        inserted=eval(input("Deposit a coin or note (in cents):\n"))
        total+=inserted
        if total>=price:
            break #Stop once sufficient or surplus of money deposited
        
        
    change=total-price
        
    while change>0:
        print("Your change is:")
        
        if change//100!=0: # // because you can have only whole number of coins & !=0 to avoid printing "0 x coins"
            print(change//100,"x $1")
        a=change%100 #You want the remainder here to carry on loop accurately
        if a//25!=0:
            print(a//25,"x 25c")
        b=a%25
        if b//10!=0:
            print(b//10,"x 10c")
        c=b%10
        if c//5!=0:
            print(c//5,"x 5c")
        d=c%5
        if d//1!=0:
            print(d//1,"x 1c")
        break #Want it to stop printing change after the first round
        
 
        
    