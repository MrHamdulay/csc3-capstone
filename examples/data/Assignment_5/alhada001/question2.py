#Adam Alhadeff ALHADA001
price = eval(input("Enter the cost (in cents):\n"))#User enters the cost of the item
given = eval(input("Deposit a coin or note (in cents):\n"))#User enters how much was paid for the item
#Conditional loop that takes place when the price is greater than what was paid
while price > given:
    given = given + eval(input("Deposit a coin or note (in cents):\n"))
#declaring blank variables
R5 = 0
R2 = 0
R1 = 0
C25 = 0
C10 = 0
C5 = 0

#Working out the change
change = given - price


#loop for when there still is change
while change > 0:
        if (change >= 500):
            change = change - 500
            R5 = R5 + 5
        elif (change >=200):
            change = change - 200
            R2 = R2 + 2
        elif (change >= 100):
            change = change - 100
            R1 = R1 + 1    
        elif (change >= 25):
            change = change - 25
            C25= C25 + 1
        elif (change >= 10):
            change = change - 10
            C10 = C10 + 1
        elif (change >= 5):
            change = change - 5
            C5 = C5 + 1   
#Printing the amount of change            

print("Your change is:")
if (R5 > 0):
    print (R5,"x","$1")
if (R2 > 0):
    print (R2,"x","$1")
if (R1 > 0):
    print (R1,"x","$1")
if (C25 > 0):
    print (C25,"x","25c")
if (C10 > 0):
    print (C10,"x","10c")
if (C5 > 0):
    print (C5,"x","5c")
                                         