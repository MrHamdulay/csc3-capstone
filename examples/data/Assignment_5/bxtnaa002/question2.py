# program to calculate change
# author: bxtnaa002
# date: 14 april 2014

cost = eval(input("Enter the cost (in cents):\n"))
#paid = eval(input("Deposit a coin or note (in cents):\n"))

totalpaid = 0

while totalpaid < cost: #if amount paid the first time does not immediately equal the cost
    morepaid = eval(input("Deposit a coin or note (in cents):\n")) #idefinite loop until the total amount paid is equal to or above cost
    totalpaid = totalpaid + morepaid
        
change = totalpaid -cost #change will be produced when total amount paid is equal to or above cost

if totalpaid > cost: #if the total paid exceeds cost, change is not equal to 0 and thus has to be calculated
    print("Your change is:")
    while change >0: #definite loop to deduce the denominations and their respective amounts of the change generated
        if change >= 100:
            a = change//100    #"//" used to integer divide the change in order to get whole numbers
            change = change - (a*100)
            print(a, "x $1")
            if change == 0: #check if new change is equal to 0 after calculating it
                break # once the change is equal to 0, the loop breaks
        if change >= 25:
            b = change//25
            change = change - (b*25)
            print(b, "x 25c")
            if change == 0:
                break
        if change >= 10:
            c = change//10
            change = change - (c*10)
            print(c, "x 10c")
            if change == 0:
                break
        if change >= 5:
            d = change//5
            change = change - (d*5)
            print(d, "x 5c")
            if change == 0:
                break  
        if change >= 1:
            e = change//1
            change = change - (e*1)
            print(e, "x 1c")
            if change == 0:
                break            
