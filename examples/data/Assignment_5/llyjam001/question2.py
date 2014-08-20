total=eval(input("Enter the cost (in cents):\n"))
paid=0

while total>paid:
    money=eval(input("Deposit a coin or note (in cents):\n"))
    paid=paid+money
    
change=paid-total

yes=False

ones=change//100
change=change-(ones*100)
if ones>0:
    yes=True    

twenties=change//25
change=change-(twenties*25)
if twenties>0:
    yes=True   

tens=change//10
change=change-(tens*10)
if tens>0:
    yes=True    

fives=change//5
change=change-(fives*5)
if fives>0:
    yes=True

cents=change
if cents>0:
    yes=True
    
if yes==True:
    print("Your change is:")
    if ones>0:
        print(ones,"x $1")
    if twenties>0:
        print(twenties,"x 25c")
    if tens>0:
        print(tens,"x 10c")    
    if fives>0:
        print(fives,"x 5c")    
    if cents>0:
        print(cents,"x 1c")
